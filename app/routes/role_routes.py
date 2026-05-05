from fastapi import APIRouter, Depends
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.dependencies.auth_dependency import get_current_user
from app.schemas.role_schema import RoleBase



router = APIRouter()

@router.post("/roles")
def create_role(data: RoleBase, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return create_role(data, db)

@router.get("/roles")
def get_all_roles(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return get_all_roles(db)

@router.get("/roles/{id}")
def get_role_by_id(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return get_role_by_id(id, db)

@router.put("/roles/{id}")
def update_role(id: int, data: RoleBase, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return update_role(id, data, db)

@router.delete("/roles/{id}")
def delete_role(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return delete_role(id, db)

