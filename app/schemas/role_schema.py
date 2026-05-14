from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str

class RoleResponse(BaseModel):
    id: int
    name: str
    created_by: int
    # created_at: str

    class Config:
        from_attributes = True
        