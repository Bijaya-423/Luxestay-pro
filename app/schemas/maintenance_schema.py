from pydantic import BaseModel


class MaintenanceCreate(BaseModel):
    room_id: int
    reported_by: int
    issue: str

class MaintenanceUpdate(BaseModel):
    room_id: int
    reported_by: int
    issue: str
    # status: str

class StatusUpdate(BaseModel):
    status: str
    