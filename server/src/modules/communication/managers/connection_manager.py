from fastapi import WebSocket

from .pull_manager import PullManager


class ConnectionManager:
    async def connect(self, websocket: WebSocket, server_id: str, user_id: str):
        await websocket.accept()

        pull_manager = PullManager()
        pull_manager.add_connection_to_pull(server_id, user_id, websocket)

    async def disconnect(self, server_id: str, user_id: str):
        pull_manager = PullManager()
        pull_manager.remove_connection_from_pull(server_id, user_id)

    async def broadcast(self, server_id: str, message: str):
        pull_manager = PullManager()
        active_connections = await pull_manager.get_active_connections(server_id)

        for _, ws in active_connections.items():
            await ws.send_text(message)


connection_singlton_manager = ConnectionManager()
