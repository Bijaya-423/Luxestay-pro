from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.order_status_schema import OrderStatusUpdate
from app.controllers import order_status_controller
from app.dependencies.auth_dependency import get_current_user


router = APIRouter()


@router.patch("/orders/{id}/status")
def update_status(id: int, data: OrderStatusUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return order_status_controller.update_order_status(id, data.status, db)


@router.get("/orders/status")
def get_status(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return order_status_controller.get_all_order_status(db)
