import uvicorn
from config.settings import settings
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(
        'src.main:app',
        host=settings.server.HOST,
        port=settings.server.PORT,
        workers=settings.server.WORKERS,
    )
