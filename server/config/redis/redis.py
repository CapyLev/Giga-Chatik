from typing import AsyncIterator

from aioredis import from_url, Redis

from ..settings import settings


async def init_redis_pool() -> AsyncIterator[Redis]:
    session = from_url(
        settings.redis.REDIS_URL,
        password=settings.redis.PASSWORD,
        encoding="utf-8",
        decode_responses=True,
    )

    yield session

    session.close()

    await session.wait_closed()
