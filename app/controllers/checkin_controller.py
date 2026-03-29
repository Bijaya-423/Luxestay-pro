from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from app.models.booking import Booking
from app.models.room import Room


#---------Check-In-------------
def check_in(data, db: Session):
    booking = db.query(Booking).filter(Booking.id == data.booking_id).first()

    if not booking:
        raise HTTPException(404, "Booking Not Found.")

    if booking.status == "checked_in":
        raise HTTPException(400, "Already checked in.")
    
    booking.actual_check_in = datetime.utcnow()
    booking.status = 'checked_in'

    #update room status
    room = db.query(Room).filter(Room.id == booking.room_id).first()

    if room:
        room.status = "occupied"

    db.commit()
    return {"message": "Checked-in Successfully."}



#----------Check-Out-------------
def check_out(data, db: Session):
    booking = db.query(Booking).filter(Booking.id == data.booking_id).first()

    if not booking:
        raise HTTPException(404, "Booking Not Found.")

    if booking.status != "checked_in":
        raise HTTPException(400, 'check-in required first.')

    booking.actual_check_out = datetime.utcnow()
    booking.status = 'checked_out'

    #update room status
    # room = db.query(Room).filter(Room.id == booking_id).first()
    room = db.query(Room).filter(Room.id == booking.room_id).first()
    

    if room:
        room.status = "available"

    db.commit()
    return {"message": "Checked-out Successfully."}


#-----------Get Check-In-------------------
def get_checkin(booking_id: int, db: Session):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(404, "Booking Not Found.")


    return{
        "booking_id": booking.id,
        "status": booking.status,
        "actual_check_in": booking.actual_check_in

        # "actual_check_in": booking.actual_check_in,
        # "actual_check_out": booking.actual_check_out,
    }

#------------Get Check-out-------------------
def get_checkout(booking_id: int, db: Session):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        raise HTTPException(404 , "Booing Not  Found.")

    return {
        "booking_id": booking.id,
        "status": booking.status,
        "actual_check_in": booking.actual_check_out
    }


# #------------Get All Check-in-------------------
# def get_all_checkin(db: Session):
#     bookings = db.query(Booking).filter(Booking.status == "checked_in").all()
#     return bookings


# #------------Get All Check-out-------------------
# def get_all_checkout(db: Session):
#     bookings = db.query(Booking).filter(Booking.status == "checked_out").all()
#     return bookings


# #------------Get All Bookings-------------------
# def get_all_bookings(db: Session):
#     bookings = db.query(Booking).all()
#     return bookings
