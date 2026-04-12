from sqlalchemy import Column, Integer, Float, String, Foreignkey
from app.models.base import BaseModel


class RestaurantBill(BaseModel):
    __tablename__ = "restaurant_bills"

    order_id = Column(Integer, Foreignkey("restaurant_orders.is"))
    total_amount = Column(Float, default=0)
    status = Column(String(50), default="unpaid")
    