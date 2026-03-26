from pydantic import BaseModel

class RoomTypeCreate(BaseModel):
    name: str
    description: str | None = None

# class RoomTypeUpdate(BaseModel):
#     name: str
#     description: str | None = None

