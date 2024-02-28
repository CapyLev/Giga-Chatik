from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.hasher import Hasher

from ..daos import ServerDAO, UserServerDAO
from ..dto import CreateServerRequestDTO, CreateServerDTO, ServerDTO


class CreateServerService:
    class CreateServerServiceException(Exception):
        pass

    class PasswordIsRequiredException(CreateServerServiceException):
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

    async def _get_default_image(self) -> str:
        return "https://inspirationseek.com/wp-content/uploads/2016/02/Cute-Alaskan-Dog.jpg"

    async def _get_hashed_password(self, password: str) -> str:
        if not password:
            raise self.PasswordIsRequiredException

        return await Hasher.hash_password(password)

    async def execute(
        self,
        user_id: str,
        request_data: CreateServerRequestDTO,
    ) -> ServerDTO:
        if not request_data.is_public:
            request_data.password = await self._get_hashed_password(
                request_data.password
            )

        request_data.image = await self._get_default_image()
        create_server_data = CreateServerDTO(
            name=request_data.name,
            image=request_data.image,
            is_public=request_data.is_public,
            password=request_data.password,
            admin_id=user_id,
        )

        server = await self._server_dao.create_server(
            session=self._session,
            server_data=create_server_data.model_dump(),
        )
        _ = await self._user_server_dao.connect_user_to_server(
            session=self._session,
            server_id=server.id,
            user_id=user_id,
        )

        return server
