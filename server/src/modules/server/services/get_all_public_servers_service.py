from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from ..daos.user_server_dao import UserServerDAO, ServerPublicShortDTO


class GetAllPublicServerService:
    def __init__(self, session: AsyncSession, user_server_dao: UserServerDAO) -> None:
        self._session = session
        self._user_server_dao = user_server_dao

    async def execute(self) -> List[ServerPublicShortDTO]:
        servers = await self._user_server_dao.get_public_servers(session=self._session)
        return servers
