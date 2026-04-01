from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.menu_item import MenuItem
from app.models.menu_category import MenuCategory

#_------------------category---------
def get_categories(db: Session):
    return db.query(MenuCategory).all()

def create_category(data, db: Session):
    obj = MenuCategory(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update_category(id: int, data, db: Session):
    obj = db.query(MenuCategory).filter(MenuCategory.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Category not found.")
    
    for key, value in data.dict().items():
        setattr(obj, key, value)
    
    db.commit()
    db.refresh(obj)
    return obj

def delete_category(id: int, db: Session):
    obj = db.query(MenuCategory).filter(MenuCategory.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Not found category")

    db.delete(obj)
    db.commit()
    # db.refresh(obj)
    return {"message": "Deleted Successfully."}

#-----------------items-------------------
def get_items(db: Session):
    return db.query(MenuItem).all()

def create_item(data, db: Session):
    obj = MenuItem(**data.dict())

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_item(id: int, db: Session):
    obj = db.query(MenuItem).filter(MenuItem.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Item not found.")

    return obj

def update_item(id: int, data, db: Session):
    obj = db.query(MenuItem).filter(MenuItem.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Item not found.")

    for key, value in data.dict().items():
        setattr(obj, key, value)
    
    db.commit()
    db.refresh(obj)
    return obj

def delete_item(id: int, db= Session):
    obj = db.query(MenuItem).filter(MenuItem.id == id).first()

    if not obj:
        raise HTTPException(status_code=404, detail="Items not found")
    
    db.delete()
    db.commit()
    return {"message": "deleted successfully."}
