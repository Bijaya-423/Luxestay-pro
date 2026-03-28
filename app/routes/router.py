from fastapi import APIRouter
from app.routes import user_routes, auth_routes, room_routes, booking_routes

api_router = APIRouter()

api_router.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
api_router.include_router(user_routes.router, prefix="/users", tags=["Users"])
api_router.include_router(room_routes.router, prefix="/room", tags=["Room"])
api_router.include_router(booking_routes.router, prefix="/booking", tags=["Booking"])
