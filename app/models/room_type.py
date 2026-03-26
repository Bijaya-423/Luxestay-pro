from sqlalchemy import Column, String
from app.models.base import BaseModel

class RoomType(BaseModel):
    __tablename__ = "room_types"

    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)