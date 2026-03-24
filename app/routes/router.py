from fastapi import APIRouter
from app.routes import user_routes, auth_routes

api_router = APIRouter()

api_router.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
api_router.include_router(user_routes.router, prefix="/users", tags=["Users"])