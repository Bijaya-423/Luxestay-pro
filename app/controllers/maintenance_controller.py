from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.maintenance_request import MaintenanceRequest


#-------------Get all------------------
def get_requests(db: Session):
    return db.query(MaintenanceRequest).all()

#-------------create-------------
def create_request(db: Session, data):
    obj = MaintenanceRequest(**data.dict())

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


#-------get by id ----------
def get_request(id: int, db: Session):
    obj = db.query(MaintenanceRequest).filter(MaintenanceRequest.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="request not found")
    
    return obj



#-------update---------
def update_request(id: int, data, db: Session):
    obj = db.query(MaintenanceRequest).filter(MaintenanceRequest.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Request not found.")

    for key, value in data.dict().items():
        setattr(obj, key, value)
    
    db.commit()
    db.refresh(obj)
    return obj




#------------------delete---------------------
def delete_request(id: int, db: Session):
    obj = db.query(MaintenanceRequest).filter(MaintenanceRequest.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Request not found.")

    obj.status = status
    db.commit()

    return obj


# ------------------update status-------------------
def update_status(id: int, status: str, db: Session):
    obj = db.query(MaintenanceRequest).filter(MaintenanceRequest.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="request not found.")

    obj.status = status
    db.commit()
    db.refresh(obj)
    return obj
