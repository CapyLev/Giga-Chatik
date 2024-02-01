from typing import Any, Dict, List, Optional, TypeVar, Union
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

PK = TypeVar("PK", bound=Union[str, UUID])
M = TypeVar("M")


class BaseRepositoryMixin:
    @classmethod
    async def find_by_pk(
        cls, session: AsyncSession, pk: PK, raise_error: bool = False
    ) -> Union["Base", bool]:
        query = select(cls).filter_by(id=pk)
        result = await cls._execute(session, query)
        instance = result.scalar()

        if instance is not None:
            return instance
        elif raise_error:
            raise NoResultFound("Instance not found")
        else:
            return False

    @classmethod
    async def find_all(cls, session: AsyncSession) -> List[Optional["Base"]]:
        query = select(cls)
        result = await cls._execute(session, query)
        return result.scalars().all()

    @classmethod
    async def create(cls, session: AsyncSession, data: Dict[str, Any]) -> "Base":
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
    ) -> List[Optional["Base"]]:
        query = select(cls).filter_by(**kwargs)
        result = await cls._execute(session, query)
        return result.scalars().all()

    @classmethod
    async def _execute(cls, session: AsyncSession, query: Any) -> Any:
        return await session.execute(query)
