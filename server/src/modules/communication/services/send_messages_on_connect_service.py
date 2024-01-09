from fastapi import WebSocket
from .daos.message_dao import MessageDAO


class SendMessagesOnConnectService:
    # TODO: добавить глобальный сервис по отправке сообщений в
    # который будет отправляться BaseModel а он будет сериализовать и помещать в вебсокет
    async def execute(self, websocket: WebSocket, message_dao: MessageDAO) -> None:
        messages = message_dao.collect_messages()
        await websocket.send_text(messages)
