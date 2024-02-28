from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.modules.auth.dto.user import UserShortDTO

from ..daos.server_dao import ServerDTO
from ..dto import ServerImageDTO, ServerPublicShortDTO, UserServerDTO
from ..models import UserServer, Server


class UserServerDAO:
    async def get_user_servers_by_user_id(
        self,
        session: AsyncSession,
        user_id: str,
    ) -> List[ServerImageDTO]:
        query = (
            select(UserServer)
            .filter_by(user_id=user_id)
            .options(joinedload(UserServer.server))
        )
        result = await UserServer.execute(session=session, query=query)
        entities = result.scalars().all()

        return [
            ServerImageDTO(
                id=str(user_server.server.id),
                image=user_server.server.image,
            )
            for user_server in entities
        ]

    async def get_public_servers(
        self,
        session: AsyncSession,
    ) -> List[ServerPublicShortDTO]:
        query = (
            select(Server)
            .filter_by(is_public=True)
            .options(joinedload(Server.user_servers))
        )
        public_server = await Server.execute(session=session, query=query)
        public_server_result = public_server.unique().scalars().all()

        return [
            ServerPublicShortDTO(
                id=str(server.id),
                image=server.image,
                desc=server.description,
                name=server.name,
                admin=UserShortDTO(
                    id=str(server.admin.id),
                    username=server.admin.username,
                ),
                count_of_members=len(server.user_servers),
            )
            for server in public_server_result
        ]

    async def is_user_already_on_server(
        self,
        session: AsyncSession,
        server_id: str,
        user_id: str,
    ) -> bool:
        is_user_already_on_server = await UserServer.find_by_parameters(
            session=session,
            user_id=user_id,
            server_id=server_id,
        )
        return True if is_user_already_on_server else False

    async def connect_user_to_server(
        self,
        session: AsyncSession,
        server_id: str,
        user_id: str,
    ) -> UserServerDTO:
        create_data = {
            "user_id": user_id,
            "server_id": server_id,
        }
        user_server = await UserServer.create(
            session=session,
            data=create_data,
        )

        query = (
            select(UserServer)
            .filter_by(id=user_server.id)
            .options(joinedload(UserServer.server))
        )

        result = await UserServer.execute(session=session, query=query)
        user_server_with_server = result.scalar()

        return UserServerDTO(
            id=user_server_with_server.id,
            user_id=user_server_with_server.user_id,
            created_at=user_server_with_server.created_at,
            server=ServerDTO.from_orm(user_server_with_server.server),
        )

    async def is_user_connected_to_server(
        self,
        session: AsyncSession,
        user_id: str,
        server_id: str,
    ) -> bool:
        user_servers_count = len(
            await UserServer.find_by_parameters(
                session=session,
                user_id=user_id,
                server_id=server_id,
            )
        )

        return bool(user_servers_count)
