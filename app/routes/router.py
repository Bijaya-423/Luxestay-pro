from fastapi import APIRouter
from app.routes import user_routes, auth_routes, room_routes, booking_routes, checkin_routes, room_rate_routes
# from app.controllers.auth_controller import get_current_user
from app.routes import housekeeping_routes, housekeeping_task_routes
from app.routes import maintenance_routes, inspection_routes

api_router = APIRouter()

api_router.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
api_router.include_router(user_routes.router, prefix="/users", tags=["Users"])
api_router.include_router(room_routes.router, prefix="/room", tags=["Room"])
api_router.include_router(booking_routes.router, prefix="/booking", tags=["Booking"])
api_router.include_router(checkin_routes.router, prefix="/stay", tags=["CheckIn/CheckOut"])
api_router.include_router(room_rate_routes.router, prefix="/rate", tags=["Room Rates"])

api_router.include_router(housekeeping_routes.router, prefix="/housekeeping", tags=["Housekeeping"])
api_router.include_router(housekeeping_task_routes.router, prefix="/housekeeping", tags=["Housekeeping Task"])
api_router.include_router(maintenance_routes.router, prefix="/maintenance", tags=["Maintenance"])

api_router.include_router(inspection_routes.router, prefix="/inspection", tags=["Inspection"])