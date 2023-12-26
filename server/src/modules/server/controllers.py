import logging

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session

from src.modules.auth.entity import UserEntity
from src.modules.auth.services import current_active_user

from .services import (
    GetServersByUserIdService,
    JoinToServerService,
    EditServerSettingsService,
)
from .dto import JoinServerRequest, EditServerRequest

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/getAll", status_code=status.HTTP_200_OK)
async def get_user_servers(
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    service = GetServersByUserIdService(session)
    result = await service.execute(user.id)
    return {"result": result}


@router.post("/join/{server_id}", status_code=status.HTTP_201_CREATED)
async def join_to_server(
    server_id: str,
    join_request_data: JoinServerRequest = None,
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    service = JoinToServerService(session)
    result = await service.execute(server_id, str(user.id), join_request_data.password)
    return {"result": result}


@router.patch("/settings/{server_id}")
async def edit_server_settings(
    server_id: str,
    server_request_data: EditServerRequest,
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    service = EditServerSettingsService(session)
    result = await service.execute(server_request_data)
    return ...
