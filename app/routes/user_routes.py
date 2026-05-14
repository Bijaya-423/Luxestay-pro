from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers import user_controller
from app.core.database import get_db
from app.dependencies.auth_dependency import get_current_user

router = APIRouter()

@router.post("/assign-role")
def assign_role_api(user_id: int, role_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return user_controller.assign_role(user_id, role_id, db, user)

#get user role
@router.get("/{user_id}/role")
def get_user_role(user_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return user_controller.get_user_role(user_id, db)

#update user role
@router.put("/{user_id}/role")
def update_user_role(user_id: int, role_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return user_controller.update_user_role(user_id, role_id, db, user)

#delete user role
@router.delete("/{user_id}/role")
def delete_user_role(user_id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return user_controller.delete_user_role(user_id, db, user)