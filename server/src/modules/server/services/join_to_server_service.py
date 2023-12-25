from typing import Never

from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.server.dto.server_dto import ServerDTO
from src.modules.server.dto.user_server_dto import UserServerDTO

from ..repository import get_user_server_repo, get_server_repo

class JoinToServerService:
    class ServerNotFound(Exception):
        def __init__(self) -> None:
            super().__init__("Could not find server. Check your server id.")

    class ServerPasswordRequired(Exception):
        def __init__(
            self,
        ) -> None:
            super().__init__("Password is required for this server.")

    class ServerPasswordInvalid(Exception):
        def __init__(self) -> None:
            super().__init__("Wrong server password provided.")

    class UserAlreadyExistsOnThisServer(Exception):
        def __init__(self) -> None:
            super().__init__("You are already a member of this server.")

    def __init__(self, session: AsyncSession) -> None:
        self.server_repo = get_server_repo(session)
        self.user_server_repo = get_user_server_repo(session)

    async def _is_server_exist(self, server_id: str) -> ServerDTO | Never:
        server = await self.server_repo.find_by_pk(server_id)

        if not server:
            raise self.ServerNotFound()

        return server

    async def _validate_private_server_password(self, password: str) -> bool:
        return True

    async def _is_user_already_on_server(self, server_id: str, user_id: str) -> bool:
        is_user_already_on_server = await self.user_server_repo.find_by_parameters(
            user_id=user_id, server_id=server_id
        )
        return True if is_user_already_on_server else False

    async def _connect_user_to_server(self, server_id: str, user_id: str) -> UserServerDTO:
        create_data = {"user_id": user_id, "server_id": server_id}
        return await self.user_server_repo.create(create_data)

    async def execute(
        self, server_id: str, user_id: str, password: str
    ) -> UserServerDTO:
        server = await self._is_server_exist(server_id)

        if not server.is_public:
            if not password:
                raise self.ServerPasswordRequired()

            is_password_valid = await self._validate_private_server_password(password)

            if not is_password_valid:
                raise self.ServerPasswordInvalid()

        is_user_already_on_server = await self._is_user_already_on_server(server_id, user_id)

        if is_user_already_on_server:
            raise self.UserAlreadyExistsOnThisServer()

        result = await self._connect_user_to_server(server_id, user_id)
        print(result)

        return result