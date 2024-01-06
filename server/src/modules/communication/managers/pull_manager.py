from typing import Dict, List, Tuple, TypeVar
from dataclasses import dataclass

from fastapi import WebSocket

from src.modules.core.utils.funcutils import get_timestamp_as_int


@dataclass(frozen=True, slots=True)
class PullData:
    ws: WebSocket
    timestamp: int


K = TypeVar("K", bound=Tuple[str, str])


class PullManager:
    def __init__(self) -> None:
        self.active_connections: Dict[K, PullData] = {}

    async def _get_key(self, server_id: str, user_id: str) -> K:
        return server_id, user_id

    async def add_connection_to_pull(
        self, server_id: str, user_id: str, ws: WebSocket
    ) -> None:
        key = await self._get_key(server_id, user_id)
        timestamp = await get_timestamp_as_int()
        self.active_connections[key] = PullData(ws, timestamp)

    async def remove_connection_from_pull(self, server_id: str, user_id: str) -> None:
        key = await self._get_key(server_id, user_id)
        if key in self.active_connections:
            del self.active_connections[key]

    async def get_active_connections(self, server_id: str) -> List[PullData]:
        connections = []
        for (s_id, u_id), data in self.active_connections.items():
            if s_id == server_id:
                connections.append(data)

        return connections


pull_manager = PullManager()
