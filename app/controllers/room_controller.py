from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.room import Room
from app.models.room_type import RoomType
from app.models.floor import Floor



#--------------------------Rooms------------------------------
def get_rooms(db: Session):
    return db.query(Room).all()

def create_room(data, db: Session):
    room = Room(**data.dict())
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

def get_room(id: int, db: Session):
    room = db.query(Room).filter(Room.id == id).first()
    if not room:
        raise HTTPException(status_code=404, detail='Room Not Found')
    return room

def update_room(id: int, data, db: Session):
    room = db.query(Room).filter(Room.id == id).first()
    if not room:
        raise HTTPException(status_code==404, detail="Room Not Found")
    
    for key, value in data.dict().items():
        setattr(room, key, value)

    db.commit()
    db.refresh(room)
    return room

def delete_room(id: int, db: Session):
    room = db.query(Room).filter(Room.id == id).first()
    if not room:
        raise HTTPException(status_code=404, detail='Room not found')
    
    db.delete(room)
    db.commit()
    return {"Message": "Deleted"}


#--------------------------Room Types------------------------------

def get_room_types(db: Session):
    return db.query(RoomType).all()

def create_room_type(data, db: Session):
    obj = RoomType(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_room_type(id: int, data, db: Session):
    obj = db.query(RoomType).filter(RoomType.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Room Type Not Found")
    
    obj.name = data.name
    obj.description = data.description

    db.commit()
    db.refresh(obj)
    return obj

def delete_room_type(id: int, db: Session):
    obj = db.query(RoomType).filter(RoomType.id == id).first()
    db.delete(obj)
    db.commit()
    return {"Message": "Deleted"}


#--------------------------Floors------------------------------

def get_floors(db: Session):
    return db.query(Floor).all()

def create_floor(data, db: Session):
    obj = Floor(**data.dict())
    db.add(obj)
    db.commit()
    # db.refresh(obj)
    return obj

def update_floor(id: int, data, db: Session):
    obj = db.query(Floor).filter(Floor.id == id).first()
    # if not obj:
    #     raise HTTPException(status_code=404, detail="Floor Not Found")
    
    obj.name = data.name
    db.commit()
    db.refresh(obj)
    return obj

def delete_floor(id: int, db: Session):
    obj = db.query(Floor).filter(Floor.id == id).first()
    db.delete(obj)
    db.commit()
    return {"Message": "Deleted"}
