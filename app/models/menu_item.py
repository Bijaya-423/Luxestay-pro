from sqlalchemy import Column, String, Integer, Float, ForeignKey, Text, Boolean
from app.models.base import BaseModel


class MenuItem(BaseModel):
    __tablename__ = "menu_items"

    category_id = Column(Integer, ForeignKey(menu_categories.id), nullable=False)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)

    description = Column(Text, nullable=False)
    is_available = Column(Boolean, default=1)

    
