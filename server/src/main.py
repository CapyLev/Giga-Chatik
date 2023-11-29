import uvicorn
from fastapi import FastAPI

from config.settings import settings

app = FastAPI(title=settings.server.NAME, **settings.server.fastapi_kwargs)

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=settings.server.HOST,
        port=settings.server.PORT,
        workers=settings.server.WORKERS,
        reload=True,
    )
