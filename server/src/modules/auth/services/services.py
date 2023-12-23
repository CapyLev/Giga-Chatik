from ..settings import fastapi_users_auth


class UserService:
    def get_current_user(self):
        return fastapi_users_auth.current_user(active=True)


user_service: UserService = UserService()
