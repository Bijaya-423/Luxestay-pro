from pydantic import BaseModel
from typing import List

class RestaurantOrderItemSchema(BaseModel):
    menu_item_id: int
    quantity: int
    price: float

class RestaurantOrderCreate(BaseModel):
    table_number: str
    items: List[RestaurantOrderItemSchema]

class RestaurantOrderUpdate(BaseModel):
    order_status: str


