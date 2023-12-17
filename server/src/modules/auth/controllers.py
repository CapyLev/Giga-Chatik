from fastapi import APIRouter


from .dto.user import UserCreate, UserRead, UserUpdate
from .settings import auth_backend, fastapi_users

router = APIRouter()


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserUpdate),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
