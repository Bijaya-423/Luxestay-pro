from sqlalchemy import Column, String
from app.models.base import BaseModel

class Floor(BaseModel):
    __tablename__ = "floors"

    name = Column(String(50), nullable=False)


    

