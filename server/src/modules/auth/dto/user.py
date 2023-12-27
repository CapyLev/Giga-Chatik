from typing import Optional

from fastapi_users.schemas import (
    BaseUser,
    BaseUserUpdate,
    CreateUpdateDictModel,
    models,
)
from pydantic import EmailStr


class UserRead(BaseUser):
    id: models.ID
    username: str
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(BaseUserUpdate):
    username: str


class UserCreate(CreateUpdateDictModel):
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
