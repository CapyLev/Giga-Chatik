from src.modules.server.utils.errors import ServerNotFoundException
from src.modules.server.repository import ServerRepository, UserServerRepository


class VerifyWSConnectionService:
    def __init__(
        self, server_repo: ServerRepository, user_server_repo: UserServerRepository
    ) -> None:
        self.server_repo = server_repo
        self.user_server_repo = user_server_repo

    async def _check_if_server_exist(self, server_id: str) -> bool:
        return await self.server_repo.find_by_pk(server_id)

    async def _check_if_user_server_exist(self, user_id: str, server_id: str) -> bool:
        user_servers_count = len(
            await self.user_server_repo.find_by_parameters(user_id, server_id)
        )

        if user_servers_count > 0:
            return True

        return False

    async def execute(self, user_id: str, server_id: str) -> bool:
        if not await self._check_if_server_exist(server_id):
            raise ServerNotFoundException()

        if not await self._check_if_user_server_exist(user_id, server_id):
            raise ServerNotFoundException()
