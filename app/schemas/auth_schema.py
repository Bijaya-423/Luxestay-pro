from pydantic import BaseModel, EmailStr, Field


class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginSchema(BaseModel):
    email: EmailStr
    
    password: str
    # password: str = Field(..., min_length=6, max_length=72)