from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.housekeeping_schema import RoomStatusUpdate
from app.controllers.housekeeping_controller import get_all_status, update_room_status
from app.dependencies.auth_dependency import get_current_user

router = APIRouter()

#-----------Get Status--------------
@router.get("/status")
def get_status(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return housekeeping_controller.get_all_status(db)


#--------------Update Status----------------
@router.patch("/housekeeping/rooms/{room_id}/status")
def update_status(room_id: int,
                    data: RoomStatusUpdate,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    return housekeeping_controller.update_room_status(room_id, data.status, db)
    