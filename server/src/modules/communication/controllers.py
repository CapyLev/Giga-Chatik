from fastapi import APIRouter, status, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session

from src.modules.server.repository import get_user_server_repo, get_server_repo
from src.modules.server.utils.errors import ServerNotFoundException
from src.modules.auth.services import current_active_user
from src.modules.auth.entity import UserEntity

from .managers import connection_singlton_manager
from .services import VerifyWSConnectionService


router = APIRouter()


@router.websocket("/ws/{server_id}")
async def chat_communication(
    websocket: WebSocket,
    server_id: str,
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    user_server_repo = get_user_server_repo(session)
    server_repo = get_server_repo(session)

    service = VerifyWSConnectionService(server_repo, user_server_repo)

    try:
        _ = service.execute(str(user.id), server_id)
    except ServerNotFoundException as exc:
        return JSONResponse(
            content={"msg": str(exc)}, status_code=status.HTTP_400_BAD_REQUEST
        )

    await connection_singlton_manager.connect(websocket, server_id, str(user.id))

    try:
        while True:
            data = await websocket.receive_text()
            await connection_singlton_manager.broadcast(
                f"Client #{str(user.id)} says: {data}"
            )
    except WebSocketDisconnect:
        connection_singlton_manager.disconnect(server_id, str(user.id))