from typing import Never, Union

from ..dto import ServerDTO
from ..repository import ServerRepository, UserServerRepository
from ..utils.errors import ServerNotFoundException, UserIsNotAdminExceptionException


class DeleteUserServerService:
    def __init__(
        self, user_server_repo: UserServerRepository, server_repo: ServerRepository
    ) -> None:
        self.server_repo = server_repo
        self.user_server_repo = user_server_repo

    async def _is_server_exist(self, server_id: str) -> Union[ServerDTO, Never]:
        server = await self.server_repo.find_by_pk(server_id)

        if not server:
            raise ServerNotFoundException()

        return server

    async def _get_user_server_id(self, server_id: str, user_id: str) -> int:
        user_server = await self.user_server_repo.find_by_parameters(
            user_id=user_id, server_id=server_id
        )

        if not user_server:
            raise ServerNotFoundException()

        return user_server[0].id

    async def _check_if_user_is_admin(self, server_admin_id: str, user_id: str) -> bool:
        return True if server_admin_id == user_id else False

    async def _delete_user_server(self, server_id: str, user_server_id: int) -> None:
        await self.user_server_repo.delete(user_server_id)
        await self.server_repo.delete(server_id)

    async def execute(self, server_id: str, user_id: str) -> None:
        server = await self._is_server_exist(server_id)
        user_server_id = await self._get_user_server_id(server_id, user_id)

        if await self._check_if_user_is_admin(server.admin_id, user_id):
            raise UserIsNotAdminExceptionException()

        await self._delete_user_server(str(server.id), user_server_id)
