from pydantic import BaseModel

class CheckInSchema(BaseModel):
    booking_id: int

class CheckOutSchema(BaseModel):
    booking_id: int
    