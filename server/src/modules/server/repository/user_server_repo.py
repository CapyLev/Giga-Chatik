from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.database.utils import get_async_session

from src.modules.core.IRepository import IRepository

from ..models import UserServer


class UserServerRepository(IRepository[UserServer]):
    pass


def get_user_server_repo(
    session: AsyncSession = Depends(get_async_session),
) -> UserServerRepository:
    return UserServerRepository(model=UserServer, session=session)
