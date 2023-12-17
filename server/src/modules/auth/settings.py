import uuid
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from .manager import get_user_manager
from .models import User

from config.settings import settings

cookie_transport = CookieTransport(
    cookie_name="4atik", cookie_max_age=settings.server.COOKIE_LIFETIME
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.server.SECRET, lifetime_seconds=settings.server.COOKIE_LIFETIME
    )


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
