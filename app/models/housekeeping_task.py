from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from app.models.base import BaseModel

class HouseKeepingTask(BaseModel):
    __tablename__ = "housekeeping_tasks"

    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    task_date = Column(Date, nullable=False)
    status = Column(String(50), default="pending")

    notes = Column(Text, nullable=True)

    