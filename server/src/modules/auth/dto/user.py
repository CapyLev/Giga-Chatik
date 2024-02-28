from datetime import datetime
from typing import Optional

from fastapi_users.schemas import (
    BaseUser,
    BaseUserUpdate,
    CreateUpdateDictModel,
    models,
)
from pydantic import EmailStr, BaseModel


class UserReadDTO(BaseUser):
    id: models.ID
    username: str
    email: EmailStr
    created_at: datetime
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdateDTO(BaseUserUpdate):
    username: str


class UserCreateDTO(CreateUpdateDictModel):
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserShortDTO(BaseModel):
    id: str
    username: str
