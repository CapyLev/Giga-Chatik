from typing import List

from src.modules.auth.dto import UserShortDTO

from ..dto import ServerPublicShortDTO
from ..repository.server_repo import ServerRepository


class GetAllPublicServerService:
    def __init__(self, server_repo: ServerRepository) -> None:
        self.server_repo = server_repo

    async def execute(self) -> List[ServerPublicShortDTO]:
        servers = await self.server_repo.get_public_servers()

        return [
            ServerPublicShortDTO(
                id=str(server.id),
                image=server.image,
                name=server.name,
                admin=UserShortDTO(
                    id=str(server.admin.id),
                    username=server.admin.username,
                ),
                count_of_members=len(server.user_servers),
            )
            for server in servers
        ]
