from datetime import datetime
from pydantic import BaseModel, UUID4

from .server_dto import ServerDTO


class UserServerDTO(BaseModel):
    id: int
    user_id: UUID4
    created_at: datetime
    server: ServerDTO
