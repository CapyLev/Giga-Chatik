from typing import List
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.core.IRepository import M, IRepository

from ..models import UserServer


class UserServerRepository(IRepository[UserServer]):
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
