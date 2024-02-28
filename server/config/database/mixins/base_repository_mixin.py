from typing import Any, Dict, List, Optional, TypeVar, Union
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

PK = TypeVar("PK", bound=Union[str, UUID])
M = TypeVar("M")


class BaseRepositoryMixin:
    @classmethod
    async def find_by_pk(
        cls,
        session: AsyncSession,
        pk: PK,
    ) -> M:
        query = select(cls).filter_by(id=pk)
        result = await cls.execute(session, query)
        instance = result.scalar()

        return instance

    @classmethod
    async def find_all(cls, session: AsyncSession) -> List[Optional[M]]:
        query = select(cls)
        result = await cls.execute(session, query)
        return result.scalars().all()

    @classmethod
    async def create(cls, session: AsyncSession, data: Dict[str, Any]) -> M:
        instance = cls(**data)
        session.add(instance)
        await session.commit()
        await session.refresh(instance)
        return instance

    @classmethod
    async def update(
        cls, session: AsyncSession, pk: PK, data: Dict[str, Any]
    ) -> Union["Base", Exception]:
        instance = await cls.find_by_pk(session, pk)

        if isinstance(instance, cls):
            for key, value in data.items():
                setattr(instance, key, value)
            await session.commit()
            await session.refresh(instance)
            return instance

        return Exception("Instance not found")

    @classmethod
    async def delete(cls, session: AsyncSession, pk: PK) -> None:
        instance = await cls.find_by_pk(session, pk)

        if isinstance(instance, cls):
            await session.delete(instance)
            await session.commit()

    @classmethod
    async def find_by_parameters(
        cls, session: AsyncSession, **kwargs
    ) -> List[Optional[M]]:
        query = select(cls).filter_by(**kwargs)
        result = await cls.execute(session, query)
        return result.scalars().all()

    @classmethod
    async def execute(cls, session: AsyncSession, query: Any) -> Any:
        return await session.execute(query)
