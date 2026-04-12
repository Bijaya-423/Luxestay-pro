from pydantic import BaseModel
from typing import List



class BillItem(BaseModel):
    menu_item_id: int
    quantity: int
    price: float


class RestaurantBillCreate(BaseModel):
    order_id: int
    items: List[BillItem]

class RestaurantBillUpdate(BaseModel):
    status: str

