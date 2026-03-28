from pydantic import BaseModel
from datetime import date


class BookingCreate(BaseModel):
    user_id: int
    room_id: int
    check_in: date
    check_out: date


class BookingUpdate(BaseModel):
    room_id: int
    check_in: date
    check_out: date
    