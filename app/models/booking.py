from sqlalchemy import Column, Integer, Date, ForeignKey
from app.models.base import BaseModel

class Booking(BaseModel):
    __tablename__ = "bookings"

    user_id = Column(Integer, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    check_in = Column(Integer, nullable=False)
    check_out = Column(Integer, nullable=False)


    