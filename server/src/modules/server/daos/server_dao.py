from typing import Union, Any, Dict

from sqlalchemy.ext.asyncio import AsyncSession

from ..dto import EditServerRequestDTO, ServerDTO
from ..models import Server


class ServerDAO:
    async def get_server_by_id(
        self, session: AsyncSession, server_id: str
    ) -> Union[ServerDTO, None]:
        server = await Server.find_by_pk(
            session=session,
            pk=server_id,
        )

        if not server:
            return

        return ServerDTO(
            id=server.id,
            name=server.name,
            image=server.image,
            is_public=server.is_public,
            password=server.password,
            admin_id=server.admin_id,
            created_at=server.created_at,
            desc=server.description,
        )

    async def update_server(
        self, session: AsyncSession, server_id: str, edit_server_data: Dict[str, Any]
    ) -> EditServerRequestDTO:
        updated_instance = await Server.update(
            session=session, pk=server_id, data=edit_server_data
        )

        return EditServerRequestDTO(
            name=updated_instance.name,
            password=updated_instance.password,
            image=updated_instance.image,
            is_public=updated_instance.is_public,
            desc=updated_instance.description,
        )

    async def delete_server(
        self,
        session: AsyncSession,
        server_id: str,
    ) -> None:
        await Server.delete(session=session, pk=server_id)

    async def create_server(
        self, session: AsyncSession, server_data: Dict[str, Any]
    ) -> ServerDTO:
        server = await Server.create(
            session=session,
            data=server_data,
        )

        return ServerDTO(
            id=str(server.id),
            name=server.name,
            image=server.image,
            desc=server.description,
            is_public=server.is_public,
            password=None,
            admin_id=str(server.admin_id),
            created_at=server.created_at,
        )
