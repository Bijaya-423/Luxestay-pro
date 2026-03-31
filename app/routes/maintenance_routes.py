from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.maintenance_schema import MaintenanceCreate, MaintenanceUpdate
from app.controllers import maintenance_controller
from app.dependencies.auth_dependency import get_current_user


router = APIRouter()




@router.get("/maintenance-requests")
def get_all(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return maintenance_controller.get_requests(db)

@router.post("/maintenance-requests")
def create(data: MaintenanceCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return maintenance_controller.create_request(data, db)

@router.get("/maintenance-requests/{id}")
def get_one(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return maintenance_controller.get_request(id, db)

@router.put("/maintenance-requests/{id}")
def update(id: int, data: MaintenanceCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return maintenance_controller.update_request(id, data, db)

@router.delete("/maintenance-requests/{id}")
def delete(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return maintenance_controller.delete_request(id, db)


@router.patch("/maintenance-requests/{id}/status")
def update_status(id: int, data: StatusUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return maintenance_controller.update_status(id, data.status, db)

    
