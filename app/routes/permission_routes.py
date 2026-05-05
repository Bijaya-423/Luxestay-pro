from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.permission_schema import PermissionCreate, PermissionUpdate, AssignPermissionSchema

from app.controllers import permission_controller
from app.dependencies.auth_dependency import get_current_user

router = APIRouter()

@router.post("/")
def create_permission(data: PermissionCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return permission_controller.create_permission(data, db)

@router.get("/")
def get_permissions(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return permission_controller.get_permissions(db)

@router.get("/{id}")
def get_permission(id, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return permission_controller.get_permission(id, db)

@router.put("/{id}")
def update_permission(id, data: PermissionUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return permission_controller.update_permission(id, data, db)

@router.delete("/{id}")
def delete_permission(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return permission_controller.delete_permission(id, db)


@router.post("/role/{role_id}")
def assign_permission(role_id: int, data: AssignPermissionSchema, db : Session = Depends(get_db), user = Depends(get_current_user)):
    return permission_controller.assign_permission_to_role(role_id, data.permission_ids, db)
