from typing import Dict, List

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from config.database.utils import get_async_session

from src.modules.auth.dto import UserReadDTO
from src.modules.auth.utils import current_active_user

from .daos import UserServerDAO, ServerDAO
from .dto import (
    EditServerRequestDTO,
    JoinServerRequestDTO,
    ServerImageDTO,
    UserServerDTO,
    CreateServerRequestDTO,
    ServerPublicShortDTO,
    ServerDTO,
)
from .services import (
    DeleteUserServerService,
    EditServerSettingsService,
    GetServersByUserIdService,
    JoinToServerService,
    CreateServerService,
    GetAllPublicServerService,
)

router = APIRouter()


@router.get(
    "/user-servers/",
    response_model=Dict[str, List[ServerImageDTO]],
    status_code=status.HTTP_200_OK,
)
async def get_user_servers(
    user: UserReadDTO = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
) -> Dict[str, List[ServerImageDTO]]:
    service = GetServersByUserIdService(
        session=session,
        user_server_dao=UserServerDAO(),
    )

    result = await service.execute(str(user.id))

    return {"result": result}


@router.get(
    "/public-servers/",
    response_model=Dict[str, List[ServerPublicShortDTO]],
    status_code=status.HTTP_200_OK,
)
async def get_public_servers(
    _: UserReadDTO = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
) -> Dict[str, List[ServerPublicShortDTO]]:
    service = GetAllPublicServerService(
        session=session,
        user_server_dao=UserServerDAO(),
    )
    result = await service.execute()

    return {"result": result}


@router.post("/join/{server_id}", response_model=UserServerDTO)
async def join_to_server(
    server_id: str,
    join_request_data: JoinServerRequestDTO = None,
    user: UserReadDTO = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
) -> UserServerDTO:
    service = JoinToServerService(
        server_dao=ServerDAO(),
        user_server_dao=UserServerDAO(),
    )

    try:
        result = await service.execute(
            server_id=server_id,
            user_id=str(user.id),
            password=join_request_data.password,
        )
    except (
        service.ServerNotFoundException,
        service.UserAlreadyExistsOnThisServerException,
    ) as exc:
        return JSONResponse(
            content={"msg": str(exc)},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    except (
        service.ServerPasswordRequiredException,
        service.ServerPasswordInvalidException,
    ) as exc:
        return JSONResponse(
            content={"msg": str(exc)},
            status_code=status.HTTP_403_FORBIDDEN,
        )

    return result


@router.patch("/settings/{server_id}", response_model=EditServerRequestDTO)
async def edit_server_settings(
    server_id: str,
    edit_server_request_data: EditServerRequestDTO,
    user: UserReadDTO = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
) -> EditServerRequestDTO:
    service = EditServerSettingsService(
        session=session,
        server_dao=ServerDAO(),
    )

    try:
        result = await service.execute(
            server_id=server_id,
            user_id=str(user.id),
            edit_server_request_data=edit_server_request_data,
        )
    except service.EditServerSettingsServiceException as exc:
        return JSONResponse(
            content={"msg": str(exc)},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return result


@router.delete("/{server_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_server(
    server_id: str,
    user: UserReadDTO = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
) -> None:
    service = DeleteUserServerService(
        session=session,
        server_dao=ServerDAO(),
    )

    try:
        _ = await service.execute(server_id, str(user.id))
    except service.DeleteUserServerServiceException as exc:
        return JSONResponse(
            content={"msg": str(exc)},
            status_code=status.HTTP_403_FORBIDDEN,
        )


@router.post(
    "",
    response_model=ServerDTO,
    status_code=status.HTTP_201_CREATED,
)
async def create_server(
    create_server_request_data: CreateServerRequestDTO,
    user: UserReadDTO = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session),
) -> ServerDTO:
    service = CreateServerService(
        session=session,
        server_dao=ServerDAO(),
        user_server_dao=UserServerDAO(),
    )

    try:
        result = await service.execute(
            user_id=str(user.id),
            request_data=create_server_request_data,
        )
    except service.CreateServerServiceException as exc:
        return JSONResponse(
            content={"msg": str(exc)},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return result
