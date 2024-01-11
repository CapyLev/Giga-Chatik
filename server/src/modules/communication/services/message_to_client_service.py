from fastapi import WebSocket

from ..dto import MessageDTO


class MessageToClientService:
    async def execute(self, websocket: WebSocket, message: MessageDTO) -> None:
        message_data = message.model_dump_json()
        await websocket.send_text(message_data)
