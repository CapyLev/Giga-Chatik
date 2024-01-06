from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel


class ServerDTO(BaseModel):
    id: str
    name: str
    image: Optional[str]
    is_public: bool
    password: Optional[str]
    admin_id: str
    created_at: datetime


class ServerImageDTO(BaseModel):
    id: str
    image: Optional[str]


class JoinServerRequestDTO(BaseModel):
    password: Optional[str]


class EditServerRequestDTO(BaseModel):
    name: Optional[str]
    password: Optional[str]
    image: Optional[str]
    is_public: Optional[bool]


class CreateServerRequestDTO(BaseModel):
    name: str
    image: Optional[str]
    is_public: bool = False
    password: Optional[str] = None


class CreateServerDTO(BaseModel):
    name: str
    image: str
    is_public: bool = False
    password: Union[str, None]
    admin_id: str
