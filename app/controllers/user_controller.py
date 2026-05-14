from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user_role import UserRole
from app.models.user import User
from app.models.role import Role

def assign_role(user_id: int, role_id: int, db: Session, current_user):
    #only admin allowed assign the role
    if current_user.type.lower() != 'admin':
        raise HTTPException(status_code=403, detail="only admin can assign thr role")
    
    #check user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    #check role exists
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found.")
    
    #Remove old role
    db.query(UserRole).filter(UserRole.user_id == user_id).delete()

    new_role = UserRole(
        user_id=user_id,
        role_id=role_id
    )
    db.add(new_role)

    #update users type
    user.type = role.name

    db.commit()
    return {"message": "Role Assigned successfully"}
    

def get_user_role(user_id: int, db: Session):
    user_role = db.query(UserRole).filter(UserRole.user_id == user_id).first()

    if not user_role:
        raise HTTPException(status_code=404, detail= "Role Not Assign")
    return user_role

def update_user_role(user_id: int, role_id: int, db: Session, current_user):
    if current_user.type.lower() != "admin":
        raise HTTPException(status_code=403, detail="Only Admin can update role")

    user_role = db.query(UserRole).filter(UserRole.user_id == user_id).first()

    if not user_role:
        raise HTTPException(status_code=404, detail="User role not found")

    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    user_role.role_id = role_id
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.type = role.name
    db.commit()
    return {"message": "User role updated successfully"}

def delete_user_role(user_id: int, db: Session, current_user):
    if current_user.type.lower() != "admin":
        raise HTTPException(status_code=403, detail="Admin only Delete the Role.")
    
    user_role = db.query(UserRole).filter(UserRole.user_id == user_id).first()

    if not user_role:
        raise HTTPException(status_code=404, detail="User Role not Found.")

    db.query(user_role)

    user = db.query(User).filter(User.id == user_id).first()

    if user:
        user.type = None
    
    db.commit()

    return {"message": "User role Removed successfully."}




























































