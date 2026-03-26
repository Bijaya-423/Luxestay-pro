# Base model (common fields)
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from app.core.database import Base


class BaseModel(Base):
    __abstract__ = True
    

    id = Column(Integer, primary_key=True, index=True)
    created_by = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    