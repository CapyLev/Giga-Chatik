from typing import Dict

from ..dto import CreateServerRequest
from ..repository import ServerRepository, UserServerRepository


class CreateServerService:
    def __init__(
        self, server_repo: ServerRepository, user_server_repo: UserServerRepository
    ) -> None:
        self.server_repo = server_repo
        self.user_server_repo = user_server_repo

    async def _get_default_image(self) -> str:
        return ""  # TODO: Get some default image

    async def _validate_server_data(
        self, user_id: str, create_server_request_data: CreateServerRequest
    ) -> Dict[str, str]:
        updated_data = create_server_request_data.dict()
        updated_data.update({"admin_id": user_id})

        if not updated_data["image"]:
            updated_data["image"] = await self._get_default_image()
        else:
            updated_data["image"] = str(updated_data["image"])

        return updated_data

    async def _get_user_server_data(
        self, user_id: str, server_id: str
    ) -> Dict[str, str]:
        return {"user_id": user_id, "server_id": server_id}

    async def execute(
        self, user_id: str, create_server_request_data: CreateServerRequest
    ) -> CreateServerRequest:
        server_data = await self._validate_server_data(
            user_id, create_server_request_data
        )

        result = await self.server_repo.create(server_data)

        user_server_data = await self._get_user_server_data(user_id, result.id)

        _ = await self.user_server_repo.create(user_server_data)

        return CreateServerRequest(
            name=result.name, image=result.image, is_public=result.is_public
        )
