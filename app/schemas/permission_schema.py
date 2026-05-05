from pydantic import BaseModel
from typing import List

class PermissionCreate(BaseModel):
    name: str

class PermissionUpdate(BaseModel):
    name: str


class AssignPermissionSchema(BaseModel):
    permission_ids: List[int]

