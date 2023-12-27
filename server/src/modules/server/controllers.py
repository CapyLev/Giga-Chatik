import logging
from typing import Dict, List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session
from src.modules.auth.entity import UserEntity
from src.modules.auth.services import current_active_user
from .dto import EditServerRequest, JoinServerRequest, ServerImageDTO, UserServerDTO
from .repository import get_user_server_repo, get_server_repo
from .services import (
    DeleteUserServerService,
    EditServerSettingsService,
    GetServersByUserIdService,
    JoinToServerService,
)
from .utils.errors import (
    ServerNotFound,
    ServerPasswordInvalid,
    ServerPasswordRequired,
    UserAlreadyExistsOnThisServer,
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
    user_server_repo = get_user_server_repo(session)
    service = GetServersByUserIdService(user_server_repo)
    result = await service.execute(user.id)
    return {"result": result}


@router.post("/join/{server_id}", response_model=UserServerDTO)
async def join_to_server(
    server_id: str,
    join_request_data: JoinServerRequest = None,
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    user_server_repo = get_user_server_repo(session)
    server_repo = get_server_repo(session)
    service = JoinToServerService(server_repo, user_server_repo)
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
    server_repo = get_server_repo(session)
    service = EditServerSettingsService(server_repo)
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
    server_repo = get_server_repo(session)
    service = DeleteUserServerService(server_repo)
    try:
        _ = await service.execute(server_id, str(user.id))
    except UserIsNotAdminException as exc:
        return Response(
            content={"msg": str(exc)}, status_code=status.HTTP_403_FORBIDDEN
        )
    return Response(status_code=status.HTTP_200_OK)
