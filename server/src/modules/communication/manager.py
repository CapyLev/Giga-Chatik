from fastapi import WebSocket


class ConnectionManager:
    async def connect(self, websocket: WebSocket, server_id: str, user_id: str):
        await websocket.accept()

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


Manager = ConnectionManager()
