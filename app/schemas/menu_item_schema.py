from pydantic import BaseModel

class MenuItemCreate(BaseModel):
    category_id: int
    name: str
    price: float
    description: str | None = None

class MenuItemUpdate(BaseModel):
    category_id: int
    name: str
    price: float
    description: str | None = None
    is_available: int

    