from sqlalchemy import Column, Integer, String, Float
from app.models.base import BaseModel


class Folio(BaseModel):
    __tablename__ = "folios"

    booking_id = Column(Integer, nullable=False)
    room_id = Column(Integer, nullable=False)

    total_amount = Column(Float, default=0)
    status = Column(String(50), nullable=False)

    # def __init__(self, booking_id, room_id, total_amount, status):
    #     self.booking_id = booking_id
    #     self.room_id = room_id
    #     self.total_amount = total_amount
    #     self.status = status

    # def __repr__(self):
    #     return f"<Folio {self.id}>"
