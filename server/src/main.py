import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


def setup_settings(application: FastAPI) -> None:
    origins = ["http://localhost", "http://localhost:3000"]
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(prefix="/api", router=routes)


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
