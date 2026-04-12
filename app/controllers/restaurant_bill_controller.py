from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.restaurant_bill_item import RestaurantBillItem
from app.models.restaurant_bill import RestaurantBill


def get_bills(db: Session):
    return db.query(RestaurantBill).all()



def create_bill(data, db: Session):
    bill = RestaurantBill(order_id=data.order_id)

    db.add(bill)
    db.commit()
    db.refresh(bill)

    total = 0

    for item in data.items:
        obj = RestaurantBillItem(
            bill_id = bill.id,
            menu_item_id = item.menu_item_id,
            quantity = item.quantity,
            price = item.price
        )
        total += item.price * item.quantity
        db.add(obj)
    bill.total_amount = total
    db.commit()
    db.refresh(bill)
    return bill



def get_bill(id: int, db: Session):
    bill = db.query(RestaurantBill).filter(RestaurantBill.id == id).first()

    if not bill:
        raise HTTPException(status_code=404, "Bill not Found.")
    
    return bill


def update_bill(id: int, data, db: Session):
    bill = db.query(RestaurantBill).filter(RestaurantBill.id == id).first()

    if not bill:
        raise HTTPException(status_code=404, details="Bill not Found.")
    
    bill.status = data.status
    db.commit()
    db.refresh(bill)
    return bill


def delete_bill(id: int, db: Session):
    bill = db.query(RestaurantBill).filter(RestaurantBill.id == id).first()

    if not bill:
        raise HTTPException(status_code=404, details="Bill not found.")

    db.delete(bill)
    db.commit()
    return {"message": "Bill deleted successfully."}
    