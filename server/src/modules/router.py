from fastapi import APIRouter

from .auth.controllers import router as auth_router
from .chat.controllers import router as chat_router
from .server.controllers import router as server_router

routes = APIRouter()

routes.include_router(auth_router, prefix="/auth", tags=["auth"])
routes.include_router(chat_router, prefix="/chat", tags=["chat"])
routes.include_router(server_router, prefix="/server", tags=["server"])
