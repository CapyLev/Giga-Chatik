from fastapi import APIRouter, status, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session

from src.modules.auth.utils import websocket_auth

from .managers import ConnectionManager
from .services import VerifyWSConnectionService
from ..auth.manager import UserManager, get_user_manager
from ..server.daos import ServerDAO, UserServerDAO

router = APIRouter()


@router.websocket("/ws/{server_id}")
async def chat_communication(
    websocket: WebSocket,
    server_id: str,
    user_manager: UserManager = Depends(get_user_manager),
    session: AsyncSession = Depends(get_async_session),
):
    access_token = websocket.headers.get("Authorization")
    user = await websocket_auth(access_token, user_manager)
    user_id = str(user.id)

    service = VerifyWSConnectionService(
        session=session,
        server_dao=ServerDAO(),
        user_server_dao=UserServerDAO(),
    )

    try:
        _ = await service.execute(user_id=user_id, server_id=server_id)
    except service.VerifyWSConnectionServiceException as exc:
        return JSONResponse(
            content={"msg": str(exc)},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    await ConnectionManager.connect(
        websocket=websocket,
        server_id=server_id,
        user_id=user_id,
    )

    try:
        while True:
            msg = await websocket.receive_text()
            await ConnectionManager.broadcast(server_id, user, msg)
    except WebSocketDisconnect:
        await ConnectionManager.disconnect(server_id, user_id)
