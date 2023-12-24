from typing import List
from sqlalchemy.ext.asyncio import AsyncSession


from ..repository.user_server_repo import get_user_server_repo
from ..dto import ServerImageDTO


class UserServerService:
    async def get_servers_by_user_id(
        self, session: AsyncSession, user_id: str
    ) -> List[ServerImageDTO]:
        user_repo = get_user_server_repo(session)
        user_servers = await user_repo.get_user_servers_by_user_id(user_id)
        return [
            ServerImageDTO(
                id=server.server.id,
                image=server.server.image,
            )
            for server in user_servers
        ]


user_server_service: UserServerService = UserServerService()
