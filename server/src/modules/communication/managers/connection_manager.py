from fastapi import WebSocket

from src.modules.auth.dto import UserReadDTO

from ..services import MessageStoreService, SendMessagesOnConnectService
from .websocket_pull_manager import websocket_pull_manager
from ..services.daos.message_dao import MessageDAO
from ..services.message_to_client_service import MessageToClientService


class ConnectionManager:
    @staticmethod
    async def connect(
        websocket: WebSocket,
        server_id: str,
        user_id: str,
    ):
        await websocket_pull_manager.add_connection_to_pull(
            server_id, user_id, websocket
        )
        await websocket.accept()

        send_message_on_connect_service = SendMessagesOnConnectService(
            message_dao=MessageDAO(),
            message_to_client_service=MessageToClientService(),
        )
        await send_message_on_connect_service.execute(websocket, server_id)

    @staticmethod
    async def disconnect(server_id: str, user_id: str):
        await websocket_pull_manager.remove_connection_from_pull(server_id, user_id)

    @staticmethod
    async def broadcast(
        server_id: str,
        user: UserReadDTO,
        message_content: str,
    ):
        active_connections = await websocket_pull_manager.get_active_connections(
            server_id
        )

        store_message_service = MessageStoreService()
        message = await store_message_service.execute(
            server_id=server_id,
            user=user,
            message_content=message_content,
        )

        for pull_data in active_connections:
            ws = pull_data.ws
            await ws.send_text(message)
