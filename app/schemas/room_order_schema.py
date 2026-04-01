from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    menu_item_id: int
    quantity: int
    price: float

class RoomOrderCreate(BaseModel):
    room_id: int
    booking_id: int | None = None
    items: List[OrderItem]

class RoomOrderUpdate(BaseModel):
    order_status: str


