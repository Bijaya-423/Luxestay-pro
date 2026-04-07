from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.user_controller import assign_role
from app.core.database import get_db
from app.dependencies.auth_dependency import get_current_user

router = APIRouter()

@router.post("/assign-role")
def assign_role_api(user_id: int, role_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return assign_role(user_id, role_id, db, user)
    