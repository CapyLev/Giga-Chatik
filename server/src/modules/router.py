from fastapi import APIRouter

from .auth.controllers import router as auth_router

routes = APIRouter()


routes.include_router(auth_router)
