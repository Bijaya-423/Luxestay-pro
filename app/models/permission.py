from sqlalchemy import Column, String, Integer
from app.models.base import BaseModel

class Permission(BaseModel):
    __tablename__ = "permissions"

    name = Column(String(191), nullable=False, unique=True)
    # created_by = Column(Integer, default=0)
