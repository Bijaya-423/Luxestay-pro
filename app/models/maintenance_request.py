from sqlalchemy import Column, Integer, String, ForeignKey, Text
from app.models.base import BaseModel

class MaintenanceRequest(BaseModel):
    __tablename__ = 'maintenance_requests'

    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    reported_by = Column(Integer, ForeignKey('users.id'), nullable=False)

    issue = Column(Text, nullable=False)
    status = Column(String(50), default="pending")

    