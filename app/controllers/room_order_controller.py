from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.room_order import RoomOrder
from app.models.room_order_item import RoomOrderItem


def get_orders(db: Session):
    return db.query(RoomOrder).all()


def create_order(data, db: Session):
    order = RoomOrder(room_id=data.room_id, booking_id=data.booking_id)
    
    db.add(order)
    db.commit()
    db.refresh(order)

    #add items
    for item in data.items:
        order_item = RoomOrderItem(order_id=order.id, menu_item_id=item.menu_item_id, quantity=item.quantity, price=item.price)
        db.add(order_item)
    
    db.commit()
    db.refresh(order)

    return order


from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.room_order import RoomOrder
from app.models.room_order_item import RoomOrderItem


def get_orders(db: Session):
    return db.query(RoomOrder).all()


def create_order(data, db: Session):
    order = RoomOrder(room_id=data.room_id, booking_id=data.booking_id)
    
    db.add(order)
    db.commit()
    db.refresh(order)

    #add items
    for item in data.items:
        order_item = RoomOrderItem(order_id=order.id, menu_item_id=item.menu_item_id, quantity=item.quantity, price=item.price)
        db.add(order_item)
    
    db.commit()
    db.refresh(order)

    return order



def get_order(id: int, db: Session):
    order = db.query(RoomOrder).filter(RoomOrder.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order Not Found.")

    return order


def update_order(id: int, data, db: Session):
    order = db.query(RoomOrder).filter(RoomOrder.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order Not Found.")

    if hasattr(data, 'order_status') and data.order_status is not None:
        order.order_status = data.order_status
    
    db.commit()
    db.refresh(order)

    return order

def delete_order(id: int, db: Session):
    order = db.query(RoomOrder).filter(RoomOrder.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found.")
    
    db.delete(order)
    db.commit()

    return {"message": "Deleted Successfully."}


def get_order(id: int, db: Session):
    order = db.query(RoomOrder).filter(RoomOrder.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order Not Found.")

    return order


def update_order(id: int, data, db: Session):
    order = db.query(RoomOrder).filter(RoomOrder.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order Not Found.")

    if hasattr(data, 'order_status') and data.order_status is not None:
        order.order_status = data.order_status
    
    db.commit()
    db.refresh(order)

    return order

def delete_order(id: int, db: Session):
    order = db.query(RoomOrder).filter(RoomOrder.id == id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found.")
    
    db.delete(order)
    db.commit()

    return {"message": "Deleted Successfully."}

