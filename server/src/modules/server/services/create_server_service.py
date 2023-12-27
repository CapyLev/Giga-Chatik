from ..dto import CreateServerRequest
from ..repository import ServerRepository, UserServerRepository


class CreateServerService:
    def __init__(
        self, server_repo: ServerRepository, user_server_repo: UserServerRepository
    ) -> None:
        self.server_repo = server_repo
        self.user_server_repo = user_server_repo

    async def execute(
        self, user_id: str, create_server_request_data: CreateServerRequest
    ) -> CreateServerService:
        create_server_request_data.admin_id = user_id
        result = await self.server_repo.create(create_server_request_data.dict())
        print(result)
        return CreateServerRequest(
            name=result.name, image=result.image, is_public=result.is_public
        )
