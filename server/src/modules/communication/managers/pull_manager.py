from typing import Dict
from fastapi import WebSocket
from config.redis_conn import RedisConnectionManager, RedisSessionType


class PullManager:
    async def _get_key(self, server_id: str, user_id: str) -> str:
        return f"{server_id}:{user_id}"

    async def add_connection_to_pull(
        self, server_id: str, user_id: str, ws: WebSocket
    ) -> None:
        key = await self._get_key(server_id, user_id)

        async with RedisConnectionManager(
            RedisSessionType.ACTIVE_CONNECTIONS_STORAGE
        ) as conn:
            await conn.hset(key, "ws_conn", ws)

    async def remove_connection_from_pull(self, server_id: str, user_id: str) -> None:
        key = await self._get_key(server_id, user_id)

        async with RedisConnectionManager(
            RedisSessionType.ACTIVE_CONNECTIONS_STORAGE
        ) as conn:
            await conn.delete(key)

    async def get_active_connections(self, server_id: str) -> Dict[str, WebSocket]:
        async with RedisConnectionManager(
            RedisSessionType.ACTIVE_CONNECTIONS_STORAGE
        ) as conn:
            keys = await conn.keys(f"{server_id}:*")
            connections = {}
            for key in keys:
                ws = await conn.hget(key, "ws_conn")
                if ws:
                    connections[key.decode("utf-8")] = ws
            return connections
