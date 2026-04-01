from sqlalchemy import Column, Integer, Float, ForeignKey
from app.models.base import BaseModel


class RestaurantOrderItem(BaseModel):
    __tablename__ = "restaurant_order_items"

    order_id = Column(Integer, ForeignKey("restaurant_order.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))

    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    # @property
    # def total_price(self):
    #     return self.quantity * self.price

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "order_id": self.order_id,
    #         "menu_item_id": self.menu_item_id,
    #         "quantity": self.quantity,
    #         "price": self.price,
    #         "total_price": self.total_price,
    #     }

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "order_id": self.order_id,
    #         "menu_item_id": self.menu_item_id,
    #         "quantity": self.quantity,
    #         "price": self.price,
    #     }

