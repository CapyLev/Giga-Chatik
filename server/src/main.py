import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.mongo import mongo_db_connection
from config.redis import redis_connection
from config.settings import settings

from .modules.router import routes


def start_application() -> FastAPI:
    application = FastAPI(
        title=settings.server.NAME,
        version=settings.server.VERSION,
        **settings.server.fastapi_kwargs,
    )

    setup_settings(application)

    return application


async def startup():
    await mongo_db_connection.init_mongo_db()
    await redis_connection.init_redis()


def setup_settings(app: FastAPI) -> None:
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_event_handler("startup", startup)
    app.include_router(prefix="/api", router=routes)


app: FastAPI = start_application()


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.server.HOST,
        port=settings.server.PORT,
        workers=settings.server.WORKERS,
        reload=True,
        log_level=settings.server.LOG_LEVEL,
    )
