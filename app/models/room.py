from sqlalchemy import Column, String, Integer, ForeignKey
from app.models.base import BaseModel
# from app.models.room_type import RoomType
# from app.models.floor import Floor


class Room(BaseModel):
    __tablename__ = 'rooms'

    room_number = Column(String(50), nullable=False)
    room_type_id = Column(Integer, ForeignKey('room_types.id'))
    floor_id = Column(Integer, ForeignKey('floors.id'))
    status = Column(String(50), default="available")   # available, occupied, maintenance

