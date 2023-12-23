from typing import Any, Dict, Generic, List, Optional, TypeVar, Union
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from config.database.base import Base

PK = TypeVar("PK")
M = TypeVar("M", bound=Base)


class IRepository(Generic[M]):
    model: Base

    def __init__(self, model: M, session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def find_by_pk(self, pk: PK) -> Union[M, Exception]:
        result = await self.session.execute(select(self.model).filter_by(id=pk))
        instance = result.scalar()

        if instance is not None:
            return instance
        else:
            return Exception("Instance not found")

    async def find_all(self) -> List[Optional[M]]:
        result = await self.session.execute(select(self.model))
        return result.scalars().all()

    async def create(self, data: Dict[str, Any]) -> M:
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def update(self, pk: PK, data: Dict[str, Any]) -> Union[M, Exception]:
        instance = await self.find_by_pk(pk)

        if isinstance(instance, self.model):
            for key, value in data.items():
                setattr(instance, key, value)
            await self.session.commit()
            await self.session.refresh(instance)
            return instance

        return Exception("Instance not found")

    async def delete(self, pk: PK) -> None:
        instance = await self.find_by_pk(pk)

        if isinstance(instance, self.model):
            self.session.delete(instance)
            await self.session.commit()

    async def find_by_parameters(self, **kwargs) -> List[Optional[M]]:
        result = await self.session.execute(select(self.model).filter_by(**kwargs))
        return result.scalars().all()
