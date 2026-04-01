from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.inspection_schema import InspectionCreate, InspectionUpdate
from app.controllers import inspection_controller

from app.dependencies.auth_dependency import get_current_user


router = APIRouter()


@router.get("/inspections")
def get_all(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return inspection_controller.get_inspections(db)

@router.post("/inspections")
def create(data: InspectionCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return inspection_controller.create_inspection(data, db)



@router.get("/inspections/{id}")
def get_by_id(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return inspection_controller.get_inspection(id, db)


@router.put("/inspections/{id}")
def update(id: int, data: InspectionUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return inspection_controller.update_inspection(id, data, db)

@router.delete("/inspections/{id}")
def delete(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return inspection_controller.delete_inspection(id, db)

