from sqlalchemy import Column, Integer, String, Float, Foreignkey
from app.models.base import BaseModel


class RestaurantBillItem(BaseModel):
    __tablename__ = "restaurant_bill_items"

    bill_id = Column(Integer, Foreignkey("restaurant_bills.id"))
    menu_item_id = Column(Integer, Foreignkey("menu_items.id"))

    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    