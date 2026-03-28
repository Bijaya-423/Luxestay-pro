from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.booking import Booking
from app.models.room import Room
from datetime import date


#---------------------Availability--------------------------
def get_available_rooms(db: Session, check_out: date, check_in: date):
    
    bookings = db.query(Booking).filter(Booking.check_in < check_out, Booking.check_out > check_in).all()

    booked_room_ids = [b.room_id for b in bookings]