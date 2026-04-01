from app.models.base import BaseModel
from sqlalchemy import Column, String

class MenuCategory(BaseModel):
    __tablename__ = "menu_categories"

    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)

