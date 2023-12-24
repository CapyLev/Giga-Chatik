from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session

from src.modules.auth.entity import UserEntity
from src.modules.auth.services import current_active_user

from .services import user_server_service

router = APIRouter()


@router.get("/getAll", status_code=status.HTTP_200_OK)
async def get_user_servers(
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    try:
        result = await user_server_service.get_servers_by_user_id(session, user.id)
        return {"result": result}
    except Exception as e:
        return {"error": "Internal Server Error"}, status.HTTP_500_INTERNAL_SERVER_ERROR
