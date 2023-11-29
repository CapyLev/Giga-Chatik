from multiprocessing import cpu_count
from typing import Any, Dict

from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    NAME: str = "auth"
    DEBUG: bool = True
    ENV_MODE: str = "dev"
    HOST: str = "0.0.0.0"
    PORT: int = "6969"
    WORKERS: int = cpu_count() * 2 - 1 if ENV_MODE == "prod" else 1

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.DEBUG,
            "docs_url": None if self.ENV_MODE != "dev" else "/docs",
            "openapi_prefix": "",
            "openapi_url": None if self.ENV_MODE != "dev" else "/openapi.json",
            "redoc_url": None if self.ENV_MODE != "dev" else "/redoc",
            "openapi_tags": None
            if self.ENV_MODE != "dev"
            else [{"name": "monitor", "description": "uptime monitor endpoints"}],
        }


class DatabaseSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.database.DB_USER}:{self.database.DB_PASS}@{self.database.DB_HOST}:{self.database.DB_PORT}/{self.database.DB_NAME}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    server: ServerSettings = ServerSettings()
    database: DatabaseSettings = DatabaseSettings()


settings = Settings()
