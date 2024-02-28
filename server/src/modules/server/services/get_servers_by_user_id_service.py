from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from ..daos.user_server_dao import UserServerDAO, ServerImageDTO


class GetServersByUserIdService:
    def __init__(self, session: AsyncSession, user_server_dao: UserServerDAO) -> None:
        self._session = session
        self._user_server_dao = user_server_dao

    async def execute(self, user_id: str) -> List[ServerImageDTO]:
        user_servers = await self._user_server_dao.get_user_servers_by_user_id(
            session=self._session, user_id=user_id
        )

        return user_servers
