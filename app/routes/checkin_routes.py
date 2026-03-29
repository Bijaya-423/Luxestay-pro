from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.checkin_schema import CheckInSchema, CheckOutSchema
from app.controllers import checkin_controller

from app.dependencies.auth_dependency import get_current_user

router = APIRouter()


#---------Check-in----------------
@router.post("/check-in")
def get_checkin(data: CheckInSchema, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return checkin_controller.check_in(data, db)


@router.get("/check-in/{booking_id}")
def get_checkin(booking_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return checkin_controller.get_checkin(booking_id, db)

#---------------check-out----------------
@router.post("/check-out")
def check_out(data: CheckOutSchema, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return checkin_controller.check_out(data, db)


@router.get("/check-out/{booking_id}")
def get_checkout(booking_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return checkin_controller.get_checkout(booking_id, db)

