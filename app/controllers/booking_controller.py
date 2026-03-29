from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.booking import Booking
from app.models.room import Room
from datetime import date


#---------------------Availability--------------------------
def get_available_rooms(check_in: date, check_out: date, db: Session):
    
    bookings = db.query(Booking).filter(Booking.check_in < check_out, Booking.check_out > check_in).all()

    booked_room_ids = [b.room_id for b in bookings]

    rooms = db.query(Room).filter(~Room.id.in_(booked_room_ids)).all()

    return rooms


#--------------------Bookings----------------------------------

def create_booking(data, db: Session):
    #check room availablility
    existing = db.query(Booking).filter(
        Booking.room_id == data.room_id,
        Booking.check_in < data.check_out,
        Booking.check_out > data.check_in
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Room Already Booked For Selected Dates.")
    
    booking = Booking(**data.dict())
    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking



def get_bookings(db: Session):
    return db.query(Booking).all()


def get_booking(id: int, db: Session):
    booking = db.query(Booking).filter(Booking.id == id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking Not Found.")
    return booking


def update_booking(id: int, data, db: Session):
    booking = db.query(Booking).filter(Booking.id == id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking Not Found.")
        
    for key, value in data.dict().items():
        setattr(booking, key, value)
    
    db.commit()
    db.refresh(booking)

    return booking

def delete_booking(id: int, db: Session):
    booking = db.query(Booking).filter(Booking.id == id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking Not Found.")

    db.delete(booking)
    db.commit()


    return {"message": "Delete Booking Successfully."}


'''
#---------------------User Bookings--------------------------   

# def get_user_bookings(user_id: int, db: Session):
#     return db.query(Booking).filter(Booking.user_id == user_id).all()


# def get_user_booking(id: int, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()
#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")
#     return booking


# def update_user_booking(id: int, data, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()

#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")
        
#     for key, value in data.dict().items():
#         setattr(booking, key, value)
    
#     db.commit()
#     db.refresh(booking)

#     return booking


# def delete_user_booking(id: int, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()

#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")

#     db.delete(booking)
#     db.commit()


#     return {"message": "Delete Booking Successfully."}


# #---------------------Admin Bookings--------------------------   

# def get_admin_bookings(db: Session):
#     return db.query(Booking).all()


# def get_admin_booking(id: int, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()
#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")
#     return booking


# def update_admin_booking(id: int, data, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()

#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")
        
#     for key, value in data.dict().items():
#         setattr(booking, key, value)
    
#     db.commit()
#     db.refresh(booking)

#     return booking


# def delete_admin_booking(id: int, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()

#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")

#     db.delete(booking)
#     db.commit()


#     return {"message": "Delete Booking Successfully."}


# #---------------------Staff Bookings--------------------------   

# def get_staff_bookings(db: Session):
#     return db.query(Booking).all()


# def get_staff_booking(id: int, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()
#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")
#     return booking


# def update_staff_booking(id: int, data, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()

#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")
        
#     for key, value in data.dict().items():
#         setattr(booking, key, value)
    
#     db.commit()
#     db.refresh(booking)

#     return booking


# def delete_staff_booking(id: int, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()

#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")

#     db.delete(booking)
#     db.commit()


#     return {"message": "Delete Booking Successfully."}


# #---------------------Manager Bookings--------------------------   

# def get_manager_bookings(db: Session):
#     return db.query(Booking).all()


# def get_manager_booking(id: int, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()
#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")
#     return booking


# def update_manager_booking(id: int, data, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()

#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")
        
#     for key, value in data.dict().items():
#         setattr(booking, key, value)
    
#     db.commit()
#     db.refresh(booking)

#     return booking


# def delete_manager_booking(id: int, db: Session):
#     booking = db.query(Booking).filter(Booking.id == id).first()

#     if not booking:
#         raise HTTPException(status_code=404, detail="Booking Not Found.")

#     db.delete(booking)
#     db.commit()


#     return {"message": "Delete Booking Successfully."}


'''