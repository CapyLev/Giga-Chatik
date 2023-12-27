from typing import Never, Union

from ..repository import ServerRepository
from ..dto import ServerDTO
from ..utils.errors import ServerNotFound, UserIsNotAdminException


class DeleteUserServerService:
    def __init__(self, server_repo: ServerRepository) -> None:
        self.server_repo = server_repo

    async def _is_server_exist(self, server_id: str) -> Union[ServerDTO, Never]:
        server = await self.server_repo.find_by_pk(server_id)

        if not server:
            raise ServerNotFound()

        return server

    async def _check_if_user_is_admin(self, server_admin_id: str, user_id: str) -> bool:
        return True if server_admin_id == user_id else False

    async def _delete_user_server(self, server_id: str) -> Union[None, Never]:
        # TODO: should i handle any error?
        await self.server_repo.delete(server_id)

    async def execute(self, server_id: str, user_id: str) -> None:
        server = await self._is_server_exist(server_id)

        if await self._check_if_user_is_admin(server.admin_id, user_id):
            raise UserIsNotAdminException()

        await self._delete_user_server(server.id)
