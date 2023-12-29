from src.modules.core.utils.hasher import Hasher

from ..dto import CreateServerRequestDTO, CreateServerDTO, UserServerCreateDTO
from ..repository import ServerRepository, UserServerRepository
from ..utils.errors import PasswordIsRequiredException


class CreateServerService:
    def __init__(
        self, server_repo: ServerRepository, user_server_repo: UserServerRepository
    ) -> None:
        self.server_repo = server_repo
        self.user_server_repo = user_server_repo

    async def _get_default_image(self) -> str:
        # TODO: Get some default image
        return "https://inspirationseek.com/wp-content/uploads/2016/02/Cute-Alaskan-Dog.jpg"

    async def _get_hashed_password(self, password: str) -> str:
        if not password:
            raise PasswordIsRequiredException()

        return await Hasher.hash_password(password)

    async def _get_create_data(
        self, request_data: CreateServerRequestDTO, admin_id: str
    ) -> CreateServerDTO:
        return CreateServerDTO(
            name=request_data.name,
            image=request_data.image,
            is_public=request_data.is_public,
            password=request_data.password,
            admin_id=admin_id,
        )

    async def _get_user_server_data(
        self, user_id: str, server_id: str
    ) -> UserServerCreateDTO:
        return UserServerCreateDTO(user_id=user_id, server_id=server_id)

    async def execute(
        self, user_id: str, request_data: CreateServerRequestDTO
    ) -> CreateServerDTO:
        if not request_data.is_public:
            request_data.password = await self._get_hashed_password(
                request_data.password
            )

        request_data.image = await self._get_default_image()

        create_server_data = await self._get_create_data(request_data, user_id)

        server = await self.server_repo.create(create_server_data.dict())

        user_server_data = await self._get_user_server_data(user_id, str(server.id))
        _ = await self.user_server_repo.create(user_server_data.dict())

        return CreateServerDTO(
            name=server.name,
            image=server.image,
            is_public=server.is_public,
            password=None,
            admin_id=server.admin_id,
        )
