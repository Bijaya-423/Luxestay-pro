from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text
from app.models.base import BaseModel


class Inspection(BaseModel):

    __tablename__ = "inspections"

    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    inspected_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    inspection_date = Column(Date, nullable=False)
    status = Column(String(50), default="good")

    remarks = Column(Text, nullable=True)

    # # Relationships
    # room = relationship("Room", back_populates="inspections")
    # inspector = relationship("User", back_populates="inspections")
