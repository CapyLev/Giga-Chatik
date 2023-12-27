from typing import List

from ..dto import ServerImageDTO, UserServerDTO
from ..repository import UserServerRepository


class GetServersByUserIdService:
    def __init__(self, user_server_repo: UserServerRepository) -> None:
        self.user_server_repo = user_server_repo

    async def _collect_user_servers_by_user_id(
        self, user_id: str
    ) -> List[UserServerDTO]:
        return await self.user_server_repo.get_user_servers_by_user_id(user_id)

    async def execute(self, user_id: str) -> List[ServerImageDTO]:
        user_servers = await self._collect_user_servers_by_user_id(user_id)

        if not user_servers:
            return []

        return [
            ServerImageDTO(
                id=server.server.id,
                image=server.server.image,
            )
            for server in user_servers
        ]
