from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.server.daos import ServerDAO, UserServerDAO


class VerifyWSConnectionService:
    class VerifyWSConnectionServiceException(Exception):
        pass

    class ServerNotFoundException(VerifyWSConnectionServiceException):
        pass

    def __init__(
        self,
        session: AsyncSession,
        server_dao: ServerDAO,
        user_server_dao: UserServerDAO,
    ) -> None:
        self._session = session
        self._server_dao = server_dao
        self._user_server_dao = user_server_dao

    async def execute(
        self,
        user_id: str,
        server_id: str,
    ) -> None:
        server = await self._server_dao.get_server_by_id(
            session=self._session, server_id=server_id
        )

        if not server:
            raise self.ServerNotFoundException

        is_user_connected_to_server = (
            await self._user_server_dao.is_user_connected_to_server(
                session=self._session,
                user_id=user_id,
                server_id=server_id,
            )
        )

        if not is_user_connected_to_server:
            raise self.ServerNotFoundException
