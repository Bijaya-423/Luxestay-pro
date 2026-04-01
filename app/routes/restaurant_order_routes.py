from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.restaurant_order_schema import RestaurantOrderCreate, RestaurantOrderUpdate
from app.controllers import restaurant_order_controller
from app.dependencies.auth_dependency import get_current_user
# from app.models.user import User




router = APIRouter()

@router.get("/restaurant-orders")
def get_orders(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return restaurant_order_controller.get_order(db)

@router.post("/restaurant-orders")
def create_order(data: RestaurantOrderCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return restaurant_order_controller.create_order(data, db)

@router.get("/restaurant-orders/{id}")
def get_order(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return restaurant_order_controller.get_order(id, db)

@router.put("/restaurant-orders/{id}")
def update_order(id: int, data: RestaurantOrderUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return restaurant_order_controller.update_order(id, data, db)



@router.delete("/restaurant-orders/{id}")

def delete_order(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return restaurant_order_controller.delete_order(id, db)
