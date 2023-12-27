from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session
from src.modules.core.IRepository import IRepository

from ..models import Server


class ServerRepository(IRepository[Server]):
    pass


def get_server_repo(
    session: AsyncSession = Depends(get_async_session),
) -> ServerRepository:
    return ServerRepository(model=Server, session=session)
