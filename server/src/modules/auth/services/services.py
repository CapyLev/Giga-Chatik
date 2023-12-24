from ..settings import fastapi_users_auth


current_active_user = fastapi_users_auth.current_user(active=True)
