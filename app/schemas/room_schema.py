from pydantic import BaseModel

class RoomCreate(BaseModel):
    room_number: str
    room_type_id: int
    floor_id: int
    
class RoomUpdate(BaseModel):
    room_number: str
    room_type_id: int
    floor_id: int

class RoomStatusUpdate(BaseModel):
    status: str

