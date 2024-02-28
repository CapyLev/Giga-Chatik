from sqlalchemy.ext.asyncio import AsyncSession

from ..daos.server_dao import ServerDAO
from ..daos.user_server_dao import UserServerDAO, UserServerDTO


class JoinToServerService:
    class JoinToServerServiceException(Exception):
        pass

    class ServerNotFoundException(JoinToServerServiceException):
        pass

    class ServerPasswordRequiredException(JoinToServerServiceException):
        pass

    class ServerPasswordInvalidException(JoinToServerServiceException):
        pass

    class UserAlreadyExistsOnThisServerException(JoinToServerServiceException):
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

    async def _validate_private_server_password(self, password: str) -> bool:
        # TODO:
        return True

    async def execute(
        self,
        server_id: str,
        user_id: str,
        password: str,
    ) -> UserServerDTO:
        server = await self._server_dao.get_server_by_id(
            session=self._session,
            server_id=server_id,
        )

        if not server:
            raise self.ServerNotFoundException

        if not server.is_public:
            if not password:
                raise self.ServerPasswordRequiredException

            is_password_valid = await self._validate_private_server_password(password)

            if not is_password_valid:
                raise self.ServerPasswordInvalidException

        is_user_already_on_server = (
            await self._user_server_dao.is_user_already_on_server(
                session=self._session,
                server_id=server_id,
                user_id=user_id,
            )
        )

        if is_user_already_on_server:
            raise self.UserAlreadyExistsOnThisServerException

        result = await self._user_server_dao.connect_user_to_server(
            session=self._session,
            server_id=server_id,
            user_id=user_id,
        )

        return result
