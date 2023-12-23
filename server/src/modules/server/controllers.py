from fastapi import APIRouter, Depends

from src.modules.auth.entity.user import UserEntity
from src.modules.auth.services import user_service

from .services import user_server_service

router = APIRouter()


@router.get("/getAll")
async def get_user_servers(
    user: UserEntity = Depends(user_service.get_current_user()),
):
    return await user_server_service.get_servers_by_user_id(user.id)
