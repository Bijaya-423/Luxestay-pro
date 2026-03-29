from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.room_rate import RoomRate


#-----------Get-------------------------
def get_room_rates(db: Session):
    return db.query(RoomRate).all()

#-----------Create-----------------
def create_room_rate(data, db: Session):
    obj = RoomRate(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

#-------------update-----------------
def update_room_rate(id: int, data, db: Session):
    obj = db.query(RoomRate).filter(RoomRate.id == id).first()

    if not obj:
        raise HTTPException(404, "Room Rate Not Found.")
    
    for key, value in  data.dict().items():
        setattr(obj, key, value)

    db.commit()
    return obj

#--------------Delete----------------
def delete_room_rate(id: int, db: Session):
    obj = db.query(RoomRate).filter(RoomRate.id == id).first()

    if not obj:
        raise HTTPException(404, "Room rate not found.")
    
    db.delete(obj)
    db.commit()

    return {"message": "Deleted Successfully."}
