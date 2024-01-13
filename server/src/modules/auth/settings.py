import uuid

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)

from config.settings import settings

from .manager import get_user_manager
from .models import User

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.server.SECRET, lifetime_seconds=settings.server.TOKEN_LIFETIME
    )


auth_backend = AuthenticationBackend(
    name="4atik",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users_auth = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
