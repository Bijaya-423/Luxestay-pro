from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.restaurant_order import RestaurantOrder
from app.models.restaurant_order_item import RestaurantOrderItem



def get_order(db: Session):
    return db.query(RestaurantOrder).all()

def create_order(data, db: Session):
    order = RestaurantOrder(table_number=data.table_number)

    db.add(order)
    db.commit()
    db.refresh(order)

    for item in data.items:
        order_item = RestaurantOrderItem(order_id=order.id,
        menu_item_id=item.menu_item_id,
        quantity=item.quantity,
        price=item.price
        )
        db.add(order_item)
    db.commit()
    db.refresh(order)
    return order

def get_order(id: int, db: Session):
    order = db.query(RestaurantOrder).filter(RestaurantOrder.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail="order not found")
    
    return order

def update_order(id: int, data, db: Session):
    order = db.query(RestaurantOrder).filter(RestaurantOrder.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail="order not found")
    
    order.order_status = data.order_status
    db.commit()

    return order



def delete_order(id: int, db: Session):
    order = db.query(RestaurantOrder).filter(RestaurantOrder.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db.delete(order)
    db.commit()

    return {"message": "deleted successfully"}

