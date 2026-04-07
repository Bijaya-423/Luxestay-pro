from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base


class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, index=True)
    # user_id = Column(Integer, ForeignKey("users.id"))
    user_id = Column(Integer, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)


    
    