from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.restaurant_bill_schema import RestaurantBillCreate, RestaurantBillUpdate
from app.controllers import restaurant_bill_controller
from app.dependencies import get_current_user


router = APIRouter()


@router.post("/restaurant-bills")
def create_bill(data: RestaurantBillCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return restaurant_bill_controller.create_bill(data, db)



@router.get("/restaurant-bills")
def get_bills(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return restaurant_bill_controller.get_bills(db)


@router.get("/restaurant-bills/{id}")
def get_bill(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return restaurant_bill_controller.get_bill(id, db)


@router.put("/restaurant-bills/{id}")
def update_bill(id: int, data: RestaurantBillUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return restaurant_bill_controller.update_bill(id, data, db)


@router.delete("/restaurant-bills/{id}")
def delete_bill(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return restaurant_bill_controller.delete_bill(id, db)


# @router.get("/restaurant-bills/{id}/pdf")
# def get_bill_pdf(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
#     return restaurant_bill_controller.get_bill_pdf(id, db)




