from pydantic import BaseModel

class OrderStatusUpdate(BaseModel):
    status: str #pending , preparing , served
    