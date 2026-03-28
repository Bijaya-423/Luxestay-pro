from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from app.core.database import get_db
from app.schemas.booking_schema import BookingCreate, BookingUpdate
from app.controllers import booking_controller


router = APIRouter()


# -------- AVAILABILITY --------
@router.get('/rooms/availability')
def get_available_rooms(check_in: date = Query(...),
                        check_out: date = Query(...),
                        db: Session = Depends(get_db)):
    return booking_controller.get_available_rooms(check_in, check_out, db)


#-----------Bookings-----------
@router.post('/bookings')
def create_booking(data: BookingCreate, db: Session = Depends(get_db)):
    return booking_controller.create_booking(data, db)


@router.get('/bookings')
def get_bookings(db: Session = Depends(get_db)):
    return booking_controller.get_bookings(db)


@router.get("/bookings/{id}")
def get_booking(id: int, db: Session = Depends(get_db)):
    return booking_controller.get_booking(id, db)

@router.put("/bookings/{id}")
def update_booking(id: int, data: BookingUpdate, db: Session = Depends(get_db)):
    return booking_controller.update_booking(id, data, db)

@router.delete("/bookings/{id}")
def delete_booking(id: int, db: Session = Depends(get_db)):
    return booking_controller.delete_booking(id, db)

    