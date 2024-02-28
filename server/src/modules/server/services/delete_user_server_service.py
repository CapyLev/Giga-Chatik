from sqlalchemy.ext.asyncio import AsyncSession

from ..daos import ServerDAO, UserServerDAO


class DeleteUserServerService:
    class DeleteUserServerServiceException(Exception):
        pass

    class ServerNotFoundException(DeleteUserServerServiceException):
        pass

    class UserIsNotServerAdminException(DeleteUserServerServiceException):
        pass

    def __init__(
        self,
        session: AsyncSession,
        server_dao: ServerDAO,
    ) -> None:
        self._session = session
        self._server_dao = server_dao
        self._user_server_dao = UserServerDAO

    async def _check_if_user_is_admin(self, server_admin_id: str, user_id: str) -> bool:
        return True if server_admin_id == user_id else False

    async def execute(self, server_id: str, user_id: str) -> None:
        server = await self._server_dao.get_server_by_id(
            session=self._session,
            server_id=server_id,
        )

        if not server:
            raise self.ServerNotFoundException

        if await self._check_if_user_is_admin(server.admin_id, user_id):
            raise self.UserIsNotServerAdminException

        await self._server_dao.delete_server(
            session=self._session, server_id=str(server.id)
        )
