from multiprocessing import cpu_count
from typing import Any, Dict, List

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    AliasChoices,
    AmqpDsn,
    BaseModel,
    Field,
    ImportString,
    PostgresDsn,
    RedisDsn,
)


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
    HOST: str = "database"
    PORT: int = 5432
    NAME: str = "postgres"
    USER: str = "postgres"
    PASS: str = "postgres"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}"


class MongoSettings(BaseSettings):
    NAME: str = Field("msgStorage", validation_alias="MONGO_INITDB_DB_NAME")
    HOST: str = Field("localhost", validation_alias="MONGO_INITDB_HOST")
    PORT: int = Field("27017", validation_alias="MONGO_INITDB_PORT")
    USER: str = Field("mongodb_user", validation_alias="MONGO_INITDB_ROOT_USERNAME")
    PASS: str = Field("mongodb_pass", validation_alias="MONGO_INITDB_ROOT_PASSWORD")

    @property
    def MONGO_URL(self) -> str:
        return f"mongodb://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    server: ServerSettings = ServerSettings()
    database: DatabaseSettings = DatabaseSettings()
    mongo: MongoSettings = MongoSettings()


settings = Settings()
