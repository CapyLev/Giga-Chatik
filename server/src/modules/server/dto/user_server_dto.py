from datetime import datetime

from pydantic import UUID4, BaseModel

from .server_dto import ServerDTO


class UserServerDTO(BaseModel):
    id: int
    user_id: UUID4
    created_at: datetime
    server: ServerDTO
