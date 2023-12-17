from fastapi import APIRouter

from .auth.controllers import router as auth_router
from .chat.controllers import router as chat_router

routes = APIRouter()


routes.include_router(auth_router)
routes.include_router(chat_router)
