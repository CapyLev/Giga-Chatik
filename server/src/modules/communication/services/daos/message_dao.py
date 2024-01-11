from typing import AsyncGenerator

from src.modules.redis import RedisConnectionManager, RedisSessionType
from src.modules.communication.dto.message_dto import MessageDTO


class MessageDAO:
    MSG_COUNT_TO_FETCH = 300

    async def collect_messages(
        self,
        server_id: str,
    ) -> AsyncGenerator[MessageDTO, None]:
        server_key = f"server:{server_id}"
        async with RedisConnectionManager(
            RedisSessionType.MSG_TEMPORARY_STORAGE
        ) as conn:
            messages = await conn.hgetall(server_key)

        for message_json in messages.values():
            message_data = MessageDTO.model_validate_json(message_json)
            yield message_data
