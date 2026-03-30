from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.housekeeping import HouseKeeping
from app.models.room import Room


#---------------Get All Status-------------------
def get_all_status(db: Session):
    return db.query(HouseKeeping).all()

#------------------Update Room Status-------------------
def update_room_status(db: Session, room_id: int, status: str):

    #check room exists
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found.")

    record = db.query(HouseKeeping).filter(HouseKeeping.room_id == room_id).first()
    if not record:
        #create new
        record = HouseKeeping(room_id=room_id, status=status)
        db.add(record)
    else:
        #update existing
        record.status = status
    
    db.commit()
    db.refresh(record)
    return record

#------------------Delete Room Status-------------------
