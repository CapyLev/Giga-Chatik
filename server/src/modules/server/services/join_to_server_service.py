from typing import Union

from ..dto import ServerDTO, UserServerDTO
from ..models import UserServer
from ..repository import ServerRepository, UserServerRepository
from ..utils.errors import (
    ServerNotFoundException,
    ServerPasswordInvalidException,
    ServerPasswordRequiredException,
    UserAlreadyExistsOnThisServerException,
)


class JoinToServerService:
    def __init__(
        self, server_repo: ServerRepository, user_server_repo: UserServerRepository
    ) -> None:
        self.server_repo = server_repo
        self.user_server_repo = user_server_repo

    async def _is_server_exist(self, server_id: str) -> Union[ServerDTO, None]:
        server = await self.server_repo.find_by_pk(server_id)

        if not server:
            raise ServerNotFoundException()

        return ServerDTO(
            id=server.id,
            name=server.name,
            image=server.image,
            is_public=server.is_public,
            password=server.password,
            admin_id=server.admin_id,
            created_at=server.created_at,
        )

    async def _validate_private_server_password(self, password: str) -> bool:
        return True

    async def _is_user_already_on_server(self, server_id: str, user_id: str) -> bool:
        is_user_already_on_server = await self.user_server_repo.find_by_parameters(
            user_id=user_id, server_id=server_id
        )
        return True if is_user_already_on_server else False

    async def _connect_user_to_server(self, server_id: str, user_id: str) -> UserServer:
        create_data = {"user_id": user_id, "server_id": server_id}
        return await self.user_server_repo.create(create_data)

    async def execute(
        self, server_id: str, user_id: str, password: str
    ) -> UserServerDTO:
        server = await self._is_server_exist(server_id)

        if not server.is_public:
            if not password:
                raise ServerPasswordRequiredException()

            is_password_valid = await self._validate_private_server_password(password)

            if not is_password_valid:
                raise ServerPasswordInvalidException()

        is_user_already_on_server = await self._is_user_already_on_server(
            server_id, user_id
        )

        if is_user_already_on_server:
            raise UserAlreadyExistsOnThisServerException()

        result = await self._connect_user_to_server(server_id, user_id)

        return UserServerDTO(
            id=result.id,
            user_id=result.user_id,
            created_at=result.created_at,
            server=ServerDTO(
                id=result.server.id,
                name=result.server.name,
                image=result.server.image,
                is_public=result.server.is_public,
                password=result.server.password,
                admin_id=result.server.admin_id,
                created_at=result.server.created_at,
            ),
        )
