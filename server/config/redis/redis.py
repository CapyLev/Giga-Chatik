from enum import Enum

from aioredis import from_url, Redis

from ..settings import settings


class RedisSessionType(Enum):
    MSG_TEMPORARY_STORAGE = 0
    ACTIVE_CONNECTIONS_STORAGE = 1
    CACHE_STORAGE = 2


class RedisClient:
    async def get_redis_session_by_type(
        self, session_type: RedisSessionType = RedisSessionType.MSG_TEMPORARY_STORAGE
    ) -> Redis:
        _redis = await from_url(
            settings.redis.REDIS_URL,
            encoding="utf-8",
            decode_responses=True,
            db=session_type.value,
        )
        return _redis


redis_client: RedisClient = RedisClient()
