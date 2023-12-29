from datetime import datetime
from typing import Optional, Union

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


class JoinServerRequestDTO(BaseModel):
    password: Optional[str]


class EditServerRequestDTO(BaseModel):
    name: Optional[str]
    password: Optional[str]
    image: Optional[HttpUrl]
    is_public: Optional[bool]


class CreateServerRequestDTO(BaseModel):
    name: str
    image: Optional[HttpUrl]
    is_public: bool = False
    password: Optional[str] = None


class CreateServerDTO(BaseModel):
    name: str
    image: str
    is_public: bool = False
    password: Union[str, None]
    admin_id: UUID4
