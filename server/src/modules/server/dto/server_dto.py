from datetime import datetime
from typing import Optional

from pydantic import BaseModel, UUID4, HttpUrl, constr


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


class JoinServerRequest(BaseModel):
    password: Optional[str]


class EditServerRequest(BaseModel):
    name: Optional[constr(max_length=70)]
    password: Optional[constr(max_length=250)]
    image: Optional[str]
    is_public: Optional[bool]
