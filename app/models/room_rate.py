from sqlalchemy import Column, Integer, Float, ForeignKey, Date, String, Boolean
from app.models.base import BaseModel

class RoomRate(BaseModel):
    __tablename__ = "room_rates"

    room_type_id = Column(Integer, ForeignKey("room_types.id"))
    price = Column(Float, nullable=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    