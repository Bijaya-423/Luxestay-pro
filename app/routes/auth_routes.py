from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth_schema import RegisterSchema, LoginSchema
from app.controllers.auth_controller import register_user, login_user
from app.core.database import get_db


router = APIRouter()


# @router.get("/test")
# def test_auth():
#     return {"message": "Auth route working ✅"}



# REGISTER
@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    return register_user(data, db)

# LOGIN
@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    return login_user(data, db)