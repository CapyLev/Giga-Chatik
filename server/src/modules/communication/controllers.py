from fastapi import APIRouter, status, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session

from src.modules.server.repository import get_user_server_repo, get_server_repo
from src.modules.server.utils.errors import ServerNotFoundException
from src.modules.auth.services import websocket_auth

from .managers import ConnectionManager
from .services import VerifyWSConnectionService
from ..auth.manager import UserManager, get_user_manager

router = APIRouter()


@router.websocket("/ws/{server_id}")
async def chat_communication(
    websocket: WebSocket,
    server_id: str,
    user_manager: UserManager = Depends(get_user_manager),
    session: AsyncSession = Depends(get_async_session),
):
    access_token = websocket.cookies.get("4atik")
    user = await websocket_auth(access_token, user_manager)
    user_id = str(user.id)

    user_server_repo = get_user_server_repo(session)
    server_repo = get_server_repo(session)

    service = VerifyWSConnectionService(server_repo, user_server_repo)

    try:
        _ = await service.execute(user_id, server_id)
    except ServerNotFoundException as exc:
        return JSONResponse(
            content={"msg": str(exc)}, status_code=status.HTTP_400_BAD_REQUEST
        )

    await ConnectionManager.connect(websocket, server_id, user_id)

    try:
        while True:
            msg = await websocket.receive_text()
            await ConnectionManager.broadcast(server_id, user, msg)
    except WebSocketDisconnect:
        await ConnectionManager.disconnect(server_id, user_id)
