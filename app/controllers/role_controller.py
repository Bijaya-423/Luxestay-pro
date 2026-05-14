from app.models.roles import Role
from fastapi import HTTPException
from sqlalchemy.orm import Session
# from app.schemas.role_schema import RoleBase

def create_role(data, db: Session, current_user):
    #only admin
    if current_user.type.lower() != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create role")

    existing_role = db.query(Role).filter(Role.name == data.name).first()
    if existing_role:
        raise HTTPException(status_code=400, detail="Role already exists")
    
    new_role = Role(
        name=data.name,
        created_by = current_user.id
    )
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

#get all role
def get_all_roles(db: Session, current_user):
    if current_user.type.lower() != "admin":
        raise HTTPException(status_code=403, detail="Only admin can fetch roles")

    roles = db.query(Role).all()
    return roles


#get role by id
def get_role_by_id(id: int, db: Session, current_user):
    if current_user.type.lower() != "admin":
        raise HTTPException(status_code=403, detail="Only admin can get role")
        
    role = db.query(Role).filter(Role.id == id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


#update role
def update_role(id: int, data, db: Session, current_user):
    if current_user.type.lower() != "admin":
        raise HTTPException(status_code=403, detail="You can not update role only admin")

    role = db.query(Role).filter(Role.id == id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    #duplicate check
    duplicate_role = db.query(Role).filter(Role.id != id, Role.name == data.name).first():
        
    
    if duplicate_role:
        raise HTTPException(status_code=400, detail="Role already exists.")

    role.name = data.name
    db.commit()
    db.refresh(role)
    return role


#delete role
def delete_role(id: int, db: Session, current_user):
    if current_user.type.lower() != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete role")
    
    role = db.query(Role).filter(Role.id == id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found.")
    
    db.delete(role)
    db.commit()
    return {"message": "Role Deleted Successfully."}
    