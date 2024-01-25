from enum import Enum

from redis.asyncio.client import Redis

from config.settings import settings


class RedisSessionType(Enum):
    MSG_TEMPORARY_STORAGE = 0
    CACHE_STORAGE = 1


class RedisConnectionManager:
    def __init__(self, session_type) -> None:
        self.connection = None
        self.session_type = session_type

    async def __aenter__(self):
        self.connection = await self._get_redis_session_by_type(self.session_type.value)
        return self.connection

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.connection.aclose()

    async def _get_redis_session_by_type(
        self,
        session_type: int,
    ) -> Redis:
        return await Redis(
            host=settings.redis.HOST,
            password=settings.redis.PASSWORD,
            port=settings.redis.PORT,
            encoding="utf-8",
            decode_responses=True,
            db=session_type,
        )
