from pydantic import BaseModel
from typing import List


class FolioItemSchema(BaseModel):
    item_type: str
    description: str | None = None
    amount: float


class FolioCreate(BaseModel):
    booking_id: int
    room_id: int
    items: List[FolioItemSchema]

class FolioUpdate(BaseModel):
    status: str

class FolioResponse(BaseModel):
    id: int
    booking_id: int
    room_id: int
    total_amount: float
    status: str
    items: List[FolioItemSchema]

    class Config:
        from_attributes = True

class FolioItemResponse(BaseModel):
    id: int
    folio_id: int
    item_type: str
    description: str | None = None
    amount: float

    class Config:
        from_attributes = True
        