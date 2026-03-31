from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.housekeeping_task_schema import TaskCreate, TaskUpdate
from app.controllers import housekeeping_task_controller
from app.dependencies.auth_dependency import get_current_user

router = APIRouter()


#-----------get all-----------
@router.get("/housekeeping/tasks")
def get_tasks(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return housekeeping_task_controller.get_tasks(db)

#-----------create-----------
@router.post("/housekeeping/tasks")
def create_task(data: TaskCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return housekeeping_task_controller.create_task(data, db)

#-----------get by id-----------
@router.get("/housekeeping/tasks/{id}")
def get_task(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return housekeeping_task_controller.get_task(id, db)

#-----------update-----------
@router.put("/housekeeping/tasks/{id}")
def update_task(id: int, data: TaskUpdate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return housekeeping_task_controller.update_task_one(id, data, db)

#-----------delete-----------
@router.delete("/housekeeping/tasks/{id}")
def delete_task(id: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return housekeeping_task_controller.delete_task(id, db)

    