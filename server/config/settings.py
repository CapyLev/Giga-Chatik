from multiprocessing import cpu_count
from typing import Any, Dict

from pydantic import Field, AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    NAME: str = "auth"
    ENV_MODE: str = "dev"
    HOST: str = "0.0.0.0"
    PORT: int = "6969"
    WORKERS: int = cpu_count() * 2 - 1 if ENV_MODE == "prod" else 1
    VERSION: str = "0.0.1"
    SECRET: str = "some ultra secret secret c:"
    COOKIE_LIFETIME: int = 86400
    LOG_LEVEL: str = "debug"

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "openapi_prefix": "",
            "redoc_url": None,
            "docs_url": None if self.ENV_MODE != "dev" else "/docs",
            "openapi_url": None if self.ENV_MODE != "dev" else "/openapi.json",
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
    def DATABASE_URL(self) -> AnyUrl:
        return f"postgresql+asyncpg://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}"


class MongoSettings(BaseSettings):
    NAME: str = Field("msgStorage", validation_alias="MONGO_INITDB_DB_NAME")
    COLLECTION: str = Field("msgStorage", validation_alias="MONGO_INITDB_COLLECTION")
    HOST: str = Field("mongodb", validation_alias="MONGO_INITDB_HOST")
    PORT: int = Field("27017", validation_alias="MONGO_INITDB_PORT")

    @property
    def MONGO_URL(self) -> str:
        return f"mongodb://{self.HOST}:{self.PORT}"


class RedisSettings(BaseSettings):
    PASSWORD: str = Field("password", validation_alias="REDIS_PASSWORD")
    HOST: str = Field("redis_conn", validation_alias="REDIS_HOST")
    PORT: int = Field(5496, validation_alias="REDIS_PORT")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    server: ServerSettings = ServerSettings()
    database: DatabaseSettings = DatabaseSettings()
    mongo: MongoSettings = MongoSettings()
    redis: RedisSettings = RedisSettings()


settings = Settings()
