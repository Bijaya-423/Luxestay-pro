from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.inspection import Inspection



#----------------get alll-------------------
def get_inspections(db: Session):
    return db.query(Inspection).all()

#------------create-------------------------
def create_inspection(data, db: Session):
    obj = Inspection(**data.dict())

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

#------------------get by id-------------------
def get_inspection(id: int, db: Session):
    obj = db.query(Inspection).filter(Inspection.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Inspection not found")
    
    return obj

#----------------update---------------------
def update_inspection(id: int, data, db: Session):
    obj = db.query(Inspection).filter(Inspection.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="INSPECTION NOT FOUND.")
    
    for key, value in data.dict().items():
        setattr(obj, key, value)
    
    db.commit()
    return obj


#--------delete-----------------
def delete_inspection(id: int, db: Session):
    obj = db.query(Inspection).filter(Inspection.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Inspection not found.")
    
    db.delete(obj)
    db.commit()

    return {"message": "Deleted successfully"}



# #-----------------search---------------------
# def search_inspection(query: str, db: Session):
#     return db.query(Inspection).filter(Inspection.remarks.ilike(f"%{query}%")).all()



# #-----------------filter by date---------------------
# def filter_inspection_by_date(date: date, db: Session):
#     return db.query(Inspection).filter(Inspection.inspection_date == date).all()
