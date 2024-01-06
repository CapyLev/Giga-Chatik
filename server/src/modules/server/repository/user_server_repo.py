from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.modules.core.BaseRepository import BaseRepository, M

from ..models import UserServer


class UserServerRepository(BaseRepository[UserServer]):
    async def get_user_servers_by_user_id(self, user_id: str) -> List[M]:
        query = (
            select(self.model)
            .options(joinedload(self.model.server))
            .filter_by(user_id=user_id)
        )
        result = await self._execute(query)
        return result.scalars().all()


def get_user_server_repo(session: AsyncSession) -> UserServerRepository:
    return UserServerRepository(model=UserServer, session=session)
