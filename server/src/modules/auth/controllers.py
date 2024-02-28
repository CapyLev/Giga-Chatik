from fastapi import APIRouter

from .dto import UserCreateDTO, UserReadDTO, UserUpdateDTO
from .settings import auth_backend, fastapi_users_auth

router = APIRouter()


router.include_router(
    fastapi_users_auth.get_auth_router(auth_backend),
    prefix="",
    tags=["auth"],
)

router.include_router(
    fastapi_users_auth.get_register_router(UserReadDTO, UserUpdateDTO),
    prefix="",
    tags=["auth"],
)

router.include_router(
    fastapi_users_auth.get_users_router(UserReadDTO, UserCreateDTO),
    prefix="",
    tags=["auth"],
)
