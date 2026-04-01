from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import BaseModel


class RoomOrder(BaseModel):
    __tablename__ = "room_orders"


    room_id = Column(Integer, ForeignKey("rooms.id"))
    booking_id = Column(Integer, nullable=True)

    order_status = Column(String(20), default="pending")

    