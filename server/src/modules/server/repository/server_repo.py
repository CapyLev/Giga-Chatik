from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session
from config.database.repository import BaseRepository

from ..models import Server


class ServerRepository(BaseRepository[Server]):
    pass


def get_server_repo(
    session: AsyncSession = Depends(get_async_session),
) -> ServerRepository:
    return ServerRepository(model=Server, session=session)
