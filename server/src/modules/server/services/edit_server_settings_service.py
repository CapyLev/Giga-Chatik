from sqlalchemy.ext.asyncio import AsyncSession

from ..daos.server_dao import ServerDAO
from ..dto import EditServerRequestDTO


class EditServerSettingsService:
    class EditServerSettingsServiceException(Exception):
        pass

    class ServerNotFoundException(EditServerSettingsServiceException):
        pass

    class UserIsNotServerAdminException(EditServerSettingsServiceException):
        pass

    def __init__(self, session: AsyncSession, server_dao: ServerDAO) -> None:
        self._session = session
        self._server_dao = server_dao

    async def _check_if_user_is_admin(self, server_admin_id: str, user_id: str) -> bool:
        return True if server_admin_id == user_id else False

    async def execute(
        self,
        server_id: str,
        user_id: str,
        edit_server_request_data: EditServerRequestDTO,
    ):
        server = await self._server_dao.get_server_by_id(
            session=self._session, server_id=server_id
        )

        if not server:
            raise self.ServerNotFoundException

        if await self._check_if_user_is_admin(server.admin_id, user_id):
            raise self.UserIsNotServerAdminException

        updated_instance = await self._server_dao.update_server(
            session=self._session,
            server_id=server_id,
            edit_server_data=edit_server_request_data.model_dump(),
        )

        return updated_instance
