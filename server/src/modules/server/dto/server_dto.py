from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, HttpUrl


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
    name: Optional[str]
    password: Optional[str]
    image: Optional[HttpUrl]
    is_public: Optional[bool]


class CreateServerRequest(BaseModel):
    name: str
    image: Optional[HttpUrl]
    is_public: Optional[bool] = False
    password: Optional[str] = None
    admin_id: Optional[UUID4] = None
