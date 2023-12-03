import uuid
from string import ascii_letters, digits
from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import (
    BaseUserManager,
    InvalidPasswordException,
    UUIDIDMixin,
    exceptions,
    models,
    schemas,
)

from config.database import get_user_db
from config.settings import settings

from .models import User


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.server.SECRET
    verification_token_secret = settings.server.SECRET

    async def validate_password(
        self, password: str, user: Union[schemas.UC, models.UP]
    ) -> None:
        if len(password) <= 8:
            raise InvalidPasswordException(
                "The password is too short. Should be more than 8 characters"
            )

        if not (set(password).difference(ascii_letters + digits)):
            raise InvalidPasswordException(
                "The password must contain at least one special character"
            )

        return

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        pass

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )

        password = user_dict.pop("password")

        user_dict["hashed_password"] = self.password_helper.hash(password)

        created_user = await self.user_db.create(user_dict)

        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
