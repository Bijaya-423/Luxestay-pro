from sqlalchemy import Column, Integer, Date, ForeignKey, DateTime, String
from app.models.base import BaseModel
from datetime import datetime


class Booking(BaseModel):
    __tablename__ = "bookings"

    user_id = Column(Integer, nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    check_in = Column(Integer, nullable=False)
    check_out = Column(Integer, nullable=False)

    #NEW FIELDS
    actual_check_in = Column(DateTime, nullable=True)
    actual_check_out = Column(DateTime, nullable=True)
    status = Column(String(50), default="booked") # booked / checked_in / checked_out
    
    # payment_status = Column(String(50), default="pending") # pending / paid / partial
    # total_amount = Column(Integer, nullable=False)
    # amount_paid = Column(Integer, default=0)
    # amount_due = Column(Integer, nullable=False)
    # payment_method = Column(String(50), nullable=True)
    # payment_date = Column(DateTime, nullable=True)
    # payment_id = Column(String(50), nullable=True)
    # payment_status = Column(String(50), default="pending") # pending / paid / partial
    # payment_status = Column(String(50), default="pending") # pending / paid / partial


    