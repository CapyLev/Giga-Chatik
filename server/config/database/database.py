from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from ..settings import settings

engine = create_async_engine(settings.database.DATABASE_URL)
Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
