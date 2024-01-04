from typing import Dict
from fastapi import WebSocket
from config.redis import redis_client, RedisSessionType


class PullManager:
    def __init__(self) -> None:
        self.redis = redis_client.get_redis_session_by_type(
            RedisSessionType.ACTIVE_CONNECTIONS_STORAGE
        )

    async def _get_key(self, server_id: str, user_id: str) -> str:
        return f"{server_id}:{user_id}"

    async def add_connection_to_pull(
        self, server_id: str, user_id: str, ws: WebSocket
    ) -> None:
        key = await self._get_key(server_id, user_id)

        async with self.redis.client() as session:
            await session.hset(key, "ws_conn", ws)

    async def remove_connection_from_pull(self, server_id: str, user_id: str) -> None:
        key = await self._get_key(server_id, user_id)

        async with self.redis.client() as session:
            await session.delete(key)

    async def get_active_connections(self, server_id: str) -> Dict[str, WebSocket]:
        async with self.redis.client() as session:
            keys = await session.keys(f"{server_id}:*")
            connections = {}
            for key in keys:
                ws = await session.hget(key, "websocket")
                if ws:
                    connections[key.decode("utf-8")] = ws
            return connections
