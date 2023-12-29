from typing import Never, Union

from ..dto import EditServerRequestDTO, ServerDTO
from ..repository import ServerRepository
from ..utils.errors import ServerNotFoundException, UserIsNotAdminExceptionException


class EditServerSettingsService:
    def __init__(self, server_repo: ServerRepository) -> None:
        self.server_repo = server_repo

    async def _is_server_exist(self, server_id: str) -> Union[ServerDTO, Never]:
        server = await self.server_repo.find_by_pk(server_id)

        if not server:
            raise ServerNotFoundException()

        return server

    async def _check_if_user_is_admin(self, server_admin_id: str, user_id: str) -> bool:
        return True if server_admin_id == user_id else False

    async def execute(
        self,
        server_id: str,
        user_id: str,
        edit_server_request_data: EditServerRequestDTO,
    ):
        server = await self._is_server_exist(server_id)

        if await self._check_if_user_is_admin(server.admin_id, user_id):
            raise UserIsNotAdminExceptionException()

        updated_instance = await self.server_repo.update(
            server_id, edit_server_request_data.dict()
        )

        return EditServerRequestDTO(
            name=updated_instance.name,
            password=updated_instance.password,
            image=updated_instance.image,
            is_public=updated_instance.is_public,
        )
