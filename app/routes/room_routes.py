from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.room_schema import RoomCreate, RoomUpdate, RoomStatusUpdate
from app.schemas.room_type_schema import RoomTypeCreate
from app.schemas.floor_schema import FloorCreate
from app.controllers import room_controller


router = APIRouter()

#----------Rooms---------------
@router.get("/rooms")
def get_rooms(db: Session = Depends(get_db)):
    return room_controller.get_rooms(db)

@router.post("/rooms")
def create_room(data: RoomCreate, db: Session = Depends(get_db)):
    return room_controller.create_room(data, db)

@router.get("/rooms/{id}")
def get_room(id: int, db: Session = Depends(get_db)):
    return room_controller.get_room(id, db)

@router.put("/rooms/{id}")
def update_room(id: int, data: RoomUpdate, db: Session = Depends(get_db)):
    return room_controller.update_room(id, data, db)

@router.delete("/rooms/{id}")
def delete_room(id: int, db: Session = Depends(get_db)):
    return room_controller.delete_room(id, db)

@router.patch("/rooms/{id}/status")
def update_status(id: int, data: RoomStatusUpdate, db: Session = Depends(get_db)):
    return room_controller.update_room_status(id, data.status, db)

#-----------------Room Types----------------------

@router.get("/room-types")
def get_types(db: Session = Depends(get_db)):
    return room_controller.get_room_types(db)

@router.post('/room-types')
def create_type(data: RoomTypeCreate, db: Session = Depends(get_db)):
    return room_controller.create_room_type(data, db)

@router.put('/room-types/{id}')
def update_type(id: int, data: RoomTypeCreate, db: Session = Depends(get_db)):
    return room_controller.update_room_type(id, data, db)

@router.delete('/room-types/{id}')
def delete_type(id: int, db: Session = Depends(get_db)):
    return room_controller.delete_room_type(id, db)


#----------------Floor--------------------
@router.get('/floors')
def get_floors(db: Session = Depends(get_db)):
    return room_controller.get_floors(db)

@router.post('/floors')
def create_floor(data: FloorCreate, db: Session = Depends(get_db)):
    return room_controller.create_floor(data, db)

@router.put('/floors/{id}')
def update_floor(id: int, data: FloorCreate, db: Session = Depends(get_db)):
    return room_controller.update_floor(id, data, db)

@router.delete('/floors/{id}')
def delete_floor(id: int, db: Session = Depends(get_db)):
    return room_controller.delete_floor(id, db)
    