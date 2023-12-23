from typing import List
from ..repository.user_server_repo import get_user_server_repo


class UserServerService:
    async def get_servers_by_user_id(self, user_id: str) -> List[dict]:
        user_repo = get_user_server_repo()
        return await user_repo.find_all()


user_server_service: UserServerService = UserServerService()
