from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.room_rate_schema import RoomRateCreate, RoomRateUpdate
from app.controllers import room_rate_controller
from app.dependencies.auth_dependency import get_current_user


router = APIRouter()


#----------Get-------------
@router.get("/room-rates")
def get_rates(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return room_rate_controller.get_room_rates(db)


#-----------Create-------------
@router.post('/room-rates')
def create_rate(data: RoomRateCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return room_rate_controller.create_room_rate(data, db)


#----------update------------------
@router.put("/room-rates/{id}")
def update_rate(id: int, data: RoomRateUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return room_rate_controller.update_room_rate(id, data, db)


#------------delete------------------
@router.delete("/room-rates/{id}")
def delete_rate(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return room_rate_controller.delete_room_rate(id, db)


