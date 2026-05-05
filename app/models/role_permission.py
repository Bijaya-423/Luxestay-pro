from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import BaseModel

class RolePermission(BaseModel):
    __tablename__ = "role_permissions"

    role_id = Column(Integer, ForeignKey("roles.id"))
    permission_id = Column(Integer, ForeignKey("permissions.id"))