from aioredis import from_url, Redis

from ..settings import settings


class RedisConnector:
    _redis = None

    async def init_redis(self) -> None:
        if not self._redis:
            self._redis = await from_url(
                settings.redis.REDIS_URL,
                password=settings.redis.PASSWORD,
                encoding="utf-8",
                decode_responses=True,
            )

    async def close_redis(self) -> None:
        if self._redis:
            self._redis.close()
            await self._redis.wait_closed()

    async def get_redis_session(self) -> Redis:
        try:
            await self.init_redis()
            yield self._redis
        finally:
            await self.close_redis()


redis_connection: RedisConnector = RedisConnector()
