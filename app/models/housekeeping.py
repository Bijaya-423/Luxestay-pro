from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.base import BaseModel

class HouseKeeping(BaseModel):
    __tablename__ = "housekeeping"

    room_id = Column(Integer, ForeignKey("rooms.id"))
    status = Column(String(50), default="clean")
    
    
    # remark = Column(String(255), nullable=True)
    # staff_id = Column(Integer, ForeignKey("staff.id"))

    # room = relationship("Room", back_populates="housekeeping")
    # staff = relationship("Staff", back_populates="housekeeping")

    # def __repr__(self):
    #     return f"<HouseKeeping {self.id} - {self.room.room_number} - {self.status}>"
