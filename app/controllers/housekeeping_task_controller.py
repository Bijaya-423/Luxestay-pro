from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.housekeeping_task import HouseKeepingTask
# from app.schemas.housekeeping_task_schema import TaskCreate, TaskUpdate


#--------Get all------------------------------------
def get_tasks(db: Session):
    return db.query(HouseKeepingTask).all()


#------------create-------------------
def create_task(data, db: Session):
    # object creation
    task = HouseKeepingTask(**data.dict())

    db.add(task)
    db.commit()
    db.refresh(task)
    return task

#------------get by id -------------------
def get_task(id: int, data, db: Session):
    task = db.query(HouseKeepingTask).filter(HouseKeepingTask.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

#-------------------update----------------------
def update_task(id: int, data, db: Session):
    task = db.query(HouseKeepingTask).filter(HouseKeepingTask.id == id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in data.dict().items():
        setattr(task, key, value)
    
    db.commit()
    db.refresh(task)
    return task


#--------------delete-----------
def delete_task(id: int, db: Session):
    task = db.query(HouseKeepingTask).filter(HouseKeepingTask.id == id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")

    db.delete(task)
    db.commit(
        
    )

    return {"message": "Deleted successfully."}


#------------------filter--------------------------
def filter_tasks(data, db: Session):
    query = db.query(HouseKeepingTask)

    if data.room_id:
        query = query.filter(HouseKeepingTask.room_id == data.room_id)
    
    if data.staff_id:
        query = query.filter(HouseKeepingTask.staff_id == data.staff_id)
    
    if data.status:
        query = query.filter(HouseKeepingTask.status == data.status)
    
    if data.task_date:
        query = query.filter(HouseKeepingTask.task_date == data.task_date)
    
    return query.all()