import logging
from typing import Dict, List

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session
from src.modules.auth.entity import UserEntity
from src.modules.auth.services import current_active_user
from .dto import (
    EditServerRequestDTO,
    JoinServerRequestDTO,
    ServerImageDTO,
    UserServerDTO,
    CreateServerRequestDTO,
    CreateServerDTO,
    ServerPublicShortDTO,
)
from .repository import get_user_server_repo, get_server_repo
from .services import (
    DeleteUserServerService,
    EditServerSettingsService,
    GetServersByUserIdService,
    JoinToServerService,
    CreateServerService,
    GetAllPublicServerService,
)
from .utils.errors import (
    ServerNotFoundException,
    ServerPasswordInvalidException,
    ServerPasswordRequiredException,
    UserAlreadyExistsOnThisServerException,
    UserIsNotAdminExceptionException,
    PasswordIsRequiredException,
)

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get(
    "/user-servers/",
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


@router.get(
    "/public-servers/",
    response_model=Dict[str, List[ServerPublicShortDTO]],
    status_code=status.HTTP_200_OK,
)
async def get_public_servers(
    _: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    user_server_repo = get_user_server_repo(session)
    service = GetAllPublicServerService(user_server_repo)
    result = await service.execute()
    return {"result": result}


@router.post("/join/{server_id}", response_model=UserServerDTO)
async def join_to_server(
    server_id: str,
    join_request_data: JoinServerRequestDTO = None,
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
        ServerNotFoundException,
        ServerPasswordRequiredException,
        ServerPasswordInvalidException,
        UserAlreadyExistsOnThisServerException,
    ) as exc:
        return JSONResponse(
            content={"msg": str(exc)}, status_code=status.HTTP_400_BAD_REQUEST
        )
    return result


@router.patch("/settings/{server_id}", response_model=EditServerRequestDTO)
async def edit_server_settings(
    server_id: str,
    edit_server_request_data: EditServerRequestDTO,
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    server_repo = get_server_repo(session)
    service = EditServerSettingsService(server_repo)
    try:
        result = await service.execute(
            server_id, str(user.id), edit_server_request_data
        )
    except (UserIsNotAdminExceptionException, ServerNotFoundException) as exc:
        return JSONResponse(
            content={"msg": str(exc)}, status_code=status.HTTP_400_BAD_REQUEST
        )
    return result


@router.delete("/{server_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_server(
    server_id: str,
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    server_repo = get_server_repo(session)
    user_server_repo = get_user_server_repo(session)
    service = DeleteUserServerService(user_server_repo, server_repo)
    try:
        _ = await service.execute(server_id, str(user.id))
    except UserIsNotAdminExceptionException as exc:
        return JSONResponse(
            content={"msg": str(exc)}, status_code=status.HTTP_403_FORBIDDEN
        )
    return


@router.post(
    "",
    response_model=CreateServerDTO,
    status_code=status.HTTP_201_CREATED,
)
async def create_server(
    create_server_request_data: CreateServerRequestDTO,
    user: UserEntity = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
):
    server_repo = get_server_repo(session)
    user_server_repo = get_user_server_repo(session)
    service = CreateServerService(server_repo, user_server_repo)
    try:
        result = await service.execute(str(user.id), create_server_request_data)
    except PasswordIsRequiredException as exc:
        print(str(exc))
        return JSONResponse(
            content={"msg": str(exc)}, status_code=status.HTTP_400_BAD_REQUEST
        )
    return result
