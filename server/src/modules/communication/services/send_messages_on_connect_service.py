from fastapi import WebSocket

from .daos.message_dao import MessageDAO
from .message_to_client_service import MessageToClientService


class SendMessagesOnConnectService:
    def __init__(
        self, message_dao: MessageDAO, message_to_client_service: MessageToClientService
    ) -> None:
        self._message_dao = message_dao
        self._message_to_client_service = message_to_client_service

    async def execute(self, websocket: WebSocket, server_id: str) -> None:
        async for message in self._message_dao.collect_messages(server_id):
            await self._message_to_client_service.execute(websocket, message)
