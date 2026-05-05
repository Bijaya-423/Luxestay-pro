from app.models.roles import Role
from fastapi import HTTPException
from sqlalchemy.orm import Session



def create_role(data, db: Session):
    role = db.query(Role).filter(Role.name == data.name).first()

    if role:
        raise HTTPException(status_code=400, detail="Role Already Exists.")

    new_role = Role(name=data.name, created_by=1)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def get_all_roles(db: Session):
    return db.query(Role).all()

def get_role_by_id(id: int, db: Session):
    return db.query(Role).filter(Role.id == id).first()


def update_role(id: int, data, db: Session):
    role = db.query(Role).filter(Role.id == id).first()

    if not role:
        raise HTTPException(status_code=404, detail="Role Not Found")
    
    if db.query(Role).filter(Role.name == data.name, Role.id != id).first():
        raise HTTPException(status_code=400, detail="Role Name Already Exists")
    
    role.name = data.name
    db.commit()
    db.refresh(role)
    return role

def delete_role(id: int, db: Session):
    role = db.query(Role).filter(Role.id == id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role Not Found.")

    db.delete(role)
    db.commit()
    return {"Message": "Deleted."}

