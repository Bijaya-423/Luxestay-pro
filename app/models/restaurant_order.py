from sqlalchemy import Column, Integer, String
from app.models.base import BaseModel

class RestaurantOrder(BaseModel):
    __tablename__ = "restaurant_orders"

    table_number = Column(String(50), nullable=False)
    order_status = Column(String(50), default="pending")
    # order_items = Column(JSON, nullable=False)
    # total_amount = Column(Float, nullable=False)
    

    