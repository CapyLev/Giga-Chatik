import logging
from typing import List, Dict

from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session

from src.modules.auth.entity import UserEntity
from src.modules.auth.services import current_active_user

from .services import (
    GetServersByUserIdService,
    JoinToServerService,
    EditServerSettingsService,
    DeleteUserServerService,
)
from .dto import JoinServerRequest, EditServerRequest, ServerImageDTO, UserServerDTO
from .utils.errors import (
    UserAlreadyExistsOnThisServer,
    ServerPasswordRequired,
    ServerPasswordInvalid,
    ServerNotFound,
    UserIsNotAdminException,
)

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get(
    "/getAll",
    response_model=Dict[str, List[ServerImageDTO]],
    status_code=status.HTTP_200_OK,
)
async def get_user_servers(
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    service = GetServersByUserIdService(session)
    result = await service.execute(user.id)
    return {"result": result}


@router.post("/join/{server_id}", response_model=UserServerDTO)
async def join_to_server(
    server_id: str,
    join_request_data: JoinServerRequest = None,
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    service = JoinToServerService(session)
    try:
        result = await service.execute(
            server_id, str(user.id), join_request_data.password
        )
    except (
        ServerNotFound,
        ServerPasswordRequired,
        ServerPasswordInvalid,
        UserAlreadyExistsOnThisServer,
    ) as exc:
        return Response(
            content={"msg": str(exc)}, status_code=status.HTTP_400_BAD_REQUEST
        )
    return result


@router.patch("/settings/{server_id}", response_model=EditServerRequest)
async def edit_server_settings(
    server_id: str,
    edit_server_request_data: EditServerRequest,
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    service = EditServerSettingsService(session)
    try:
        result = await service.execute(
            server_id, str(user.id), edit_server_request_data
        )
    except (UserIsNotAdminException, ServerNotFound) as exc:
        return Response(
            content={"msg": str(exc)}, status_code=status.HTTP_400_BAD_REQUEST
        )
    return result


@router.delete("/{server_id}")
async def delete_server(
    server_id: str,
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    service = DeleteUserServerService(session)
    try:
        _ = await service.execute(server_id, str(user.id))
    except UserIsNotAdminException as exc:
        return Response(
            content={"msg": str(exc)}, status_code=status.HTTP_403_FORBIDDEN
        )
    return Response(status_code=status.HTTP_200_OK)
