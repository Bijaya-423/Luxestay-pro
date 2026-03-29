from pydantic import BaseModel
from datetime import date


class RoomRateCreate(BaseModel):
    room_type_id: int
    price: float
    start_date: date | None = None
    end_date: date | None = None

class RoomRateUpdate(BaseModel):
    room_type_id: int
    price: float
    start_date: date | None = None
    end_date: date | None = None

# class RoomRateResponse(BaseModel):
#     id: int
#     room_type_id: int
#     price: float
#     start_date: date | None = None
#     end_date: date | None = None

#     class Config:
#         from_attributes = True
