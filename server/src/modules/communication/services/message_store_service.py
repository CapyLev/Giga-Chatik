from src.modules.auth.entity import UserEntity
from src.modules.auth.dto import UserShortDTO
from src.modules.redis import RedisConnectionManager, RedisSessionType
from src.modules.core.utils.funcutils import get_uuid_as_str, get_timestamp_as_int
from src.modules.communication.dto import MessageDTO


class MessageStoreService:
    async def _create_message(
        self, server_id: str, user_short_info: UserShortDTO, message_content: str
    ) -> MessageDTO:
        message_id = await get_uuid_as_str()
        timestamp = await get_timestamp_as_int()

        return MessageDTO(
            id=message_id,
            user=user_short_info,
            server_id=server_id,
            content=message_content,
            timestamp=timestamp,
            id_deleted=False,
            attachments=[],
        )

    async def execute(
        self, server_id: str, user: UserEntity, message_content: str
    ) -> str:
        user_short_info = UserShortDTO(id=str(user.id), username=user.username)

        message = await self._create_message(
            server_id, user_short_info, message_content
        )
        message_json = message.model_dump_json()

        async with RedisConnectionManager(
            RedisSessionType.MSG_TEMPORARY_STORAGE
        ) as conn:
            server_key = f"server:{message.server_id}"
            message_key = f"message:{message.id}"
            await conn.hset(server_key, message_key, message_json)

        return message_json
