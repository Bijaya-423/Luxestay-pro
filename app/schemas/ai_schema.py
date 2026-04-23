from pydantic import BaseModel

class AIRequest(BaseModel):
    message: str