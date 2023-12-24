from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4, HttpUrl


class ServerDTO(BaseModel):
    id: UUID4
    name: str
    image: Optional[HttpUrl]
    is_public: bool
    password: Optional[str]
    admin_id: UUID4
    created_at: datetime


class ServerImageDTO(BaseModel):
    id: UUID4
    image: Optional[HttpUrl]
