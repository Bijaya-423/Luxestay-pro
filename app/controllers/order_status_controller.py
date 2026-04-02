from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.room_order import RoomOrder
from app.models.restaurant_order import RestaurantOrder


def update_order_status(order_id: int, status: str, db: Session):
    order = db.query(RoomOrder).filter(RoomOrder.id == order_id).first()

    if order:
        order.order_status = status
        db.commit()
        db.refresh(order)
        return {"message": "Room order status updated", "order_id": order_id}

    
    else:
        raise HTTPException(status_code=404, detail="Order not found.")

    
    order = db.query(RestaurantOrder).filter(RestaurantOrder.id == order_id).first()

    if order:
        order.order_status = status
        db.commit()
        return {"message": "Restaurant order status updated.", "order_id": order_id}
    # else:
    
    raise HTTPException(status_code=404, detail="Order not found.")


def get_all_order_status(db: Session):
    room_orders = db.query(RoomOrder).all()
    restaurant_orders = db.query(RestaurantOrder).all()


    return {
        "room_orders": [
            {"id": o.id, "status": o.order_status} for o in room_orders
        ], 
        "restaurant_orders": [
            {"id": o.id, "status": o.order_status} for o in restaurant_orders
        ]
    }
        
    