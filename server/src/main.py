import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.settings import settings

from .modules.router import routes


def start_application() -> FastAPI:
    app = FastAPI(
        title=settings.server.NAME,
        version=settings.server.VERSION,
        **settings.server.fastapi_kwargs
    )

    setup_settings(app)

    return app


def setup_settings(app: FastAPI) -> None:
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router=routes)


app: FastAPI = start_application()

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.server.HOST,
        port=settings.server.PORT,
        workers=settings.server.WORKERS,
        reload=True,
    )
