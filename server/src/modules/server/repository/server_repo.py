from typing import List

from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session
from config.database.repository import BaseRepository

from ..models import Server


class ServerRepository(BaseRepository[Server]):
    async def get_public_servers(self) -> List[Server]:
        query = (
            select(self.model)
            .filter_by(is_public=True)
            .options(joinedload(self.model.user_servers))
        )
        result = await self._execute(query)
        return result.unique().scalars().all()


def get_server_repo(
    session: AsyncSession = Depends(get_async_session),
) -> ServerRepository:
    return ServerRepository(model=Server, session=session)
