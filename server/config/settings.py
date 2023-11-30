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
    VERSION: str = "0.0.1"
    SECRET: str = "some ultra secret secret c:"
    COOKIE_LIFETIME: int = 3600

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
    DB_HOST: str = "database"
    DB_PORT: int = 5432
    DB_NAME: str = "postgres"
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    server: ServerSettings = ServerSettings()
    database: DatabaseSettings = DatabaseSettings()


settings = Settings()
