from multiprocessing import cpu_count
from typing import Any, Dict

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ServerSettings(BaseSettings):
    NAME: str = "auth"
    ENV_MODE: str = "dev"
    HOST: str = "0.0.0.0"
    PORT: int = "6969"
    WORKERS: int = cpu_count() * 2 - 1 if ENV_MODE == "prod" else 1
    VERSION: str = "0.0.1"
    SECRET: str = "some ultra secret secret c:"
    TOKEN_LIFETIME: int = 86400
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
    HOST: str = Field("postgres", validation_alias="DB_HOST")
    PORT: int = Field(6432, validation_alias="DB_PORT")
    NAME: str = Field("postgres", validation_alias="DB_NAME")
    USER: str = Field("postgres", validation_alias="DB_USER")
    PASS: str = Field("postgres", validation_alias="DB_PASSWORD")

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}"


class MongoSettings(BaseSettings):
    NAME: str = Field("gigachatik", validation_alias="MONGO_INITDB_DB_NAME")
    COLLECTION: str = Field("msgStorage", validation_alias="MONGO_INITDB_COLLECTION")
    HOST: str = Field("mongodb", validation_alias="MONGO_INITDB_HOST")
    PORT: int = Field("27017", validation_alias="MONGO_INITDB_PORT")

    @property
    def MONGO_URL(self) -> str:
        return f"mongodb://{self.HOST}:{self.PORT}"


class RedisSettings(BaseSettings):
    PASSWORD: str = Field("password", validation_alias="REDIS_PASSWORD")
    HOST: str = Field("redis", validation_alias="REDIS_HOST")
    PORT: int = Field(5496, validation_alias="REDIS_PORT")


class ExtraSettings(BaseSettings):
    BETTER_STACK_LOGS_TOKEN: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.server")

    server: ServerSettings = ServerSettings()
    database: DatabaseSettings = DatabaseSettings()
    mongo: MongoSettings = MongoSettings()
    redis: RedisSettings = RedisSettings()
    extra: ExtraSettings = ExtraSettings()


settings = Settings()
