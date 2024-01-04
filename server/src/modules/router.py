from fastapi import APIRouter

from .auth.controllers import router as auth_router
from .communication.controllers import router as communication_router
from .server.controllers import router as server_router

routes = APIRouter()

routes.include_router(auth_router, prefix="/auth", tags=["auth"])
routes.include_router(communication_router, prefix="/communication", tags=["chat"])
routes.include_router(server_router, prefix="/server", tags=["server"])
