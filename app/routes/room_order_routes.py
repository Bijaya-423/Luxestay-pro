from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.room_order_schema import RoomOrderCreate, RoomOrderUpdate
from app.controllers import room_order_controller
from app.dependencies.auth_dependency import get_current_user
from app.models.user import User

router = APIRouter()


@router.get("/room_orders")
def get_orders(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return room_order_controller.get_orders(db)


@router.post("/room_orders")
def create_order(data: RoomOrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return room_order_controller.create_order(data, db)


@router.get("/room_orders/{id}")
def get_order(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return room_order_controller.get_order(id, db)


@router.put("/room_orders/{id}")
def update_order(id: int, data: RoomOrderUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return room_order_controller.update_order(id, data, db)


@router.delete("/room_orders/{id}")
def delete_order(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return room_order_controller.delete_order(id, db)

