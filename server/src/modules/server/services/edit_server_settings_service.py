from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.server.repository import get_server_repo


class EditServerSettingsService:
    def __init__(self, session: AsyncSession) -> None:
        self.server_repo = get_server_repo(session)

    def execute(self):
        ...
