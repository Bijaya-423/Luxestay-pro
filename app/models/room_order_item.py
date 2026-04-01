from sqlalchemy import Column, Integer, Float, ForeignKey
from app.models.base import BaseModel



class RoomOrderItem(BaseModel):
    __tablename__ = "room_order_items"

    order_id = Column(Integer, ForeignKey("room_orders.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))

    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    