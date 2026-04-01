from pydantic import BaseModel
from datetime import date


class InspectionCreate(BaseModel):
    room_id: int
    inspected_by: int
    inspection_date: date
    remarks: str | None = None



class InspectionUpdate(BaseModel):
    room_id: int
    inspected_by: int
    inspection_date: date
    status: str
    remarks: str | None = None





