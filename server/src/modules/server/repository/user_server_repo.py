from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from config.database.repository import BaseRepository

from ..models import UserServer


class UserServerRepository(BaseRepository[UserServer]):
    async def get_user_servers_by_user_id(self, user_id: str) -> List[UserServer]:
        query = (
            select(self.model)
            .filter_by(user_id=user_id)
            .options(joinedload(self.model.server))
        )
        result = await self._execute(query)
        return result.scalars().all()


def get_user_server_repo(session: AsyncSession) -> UserServerRepository:
    return UserServerRepository(model=UserServer, session=session)
