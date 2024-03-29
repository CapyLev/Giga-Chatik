from typing import Union

from fastapi import HTTPException

from ..entity import UserEntity
from ..manager import UserManager
from ..settings import fastapi_users_auth, get_jwt_strategy

current_active_user = fastapi_users_auth.current_user(active=True)


async def websocket_auth(
    token: str, user_manager: UserManager
) -> Union[UserEntity, Exception]:
    if not token:
        raise HTTPException(status_code=401, detail="Token is missing")

    jwt_strategy = get_jwt_strategy()

    user = await jwt_strategy.read_token(token.split()[-1], user_manager)

    if user and user.is_active:
        return user

    raise HTTPException(status_code=401, detail="Invalid or inactive user token")
