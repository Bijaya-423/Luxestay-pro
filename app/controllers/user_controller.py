from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user_role import UserRole
from app.models.user import User
from app.models.role import Role

def assign_role(user_id: int, role_id: int, db: Session):
    #only admin allowed assign the role
    if current_user.type != 'admin':
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
    db.commit()
    return {"message": "Role Assigned successfully"}
    






























































# # GET ALL USERS
# def get_all_users(db: Session):
#     users = db.query(User).all()
#     return users


# # GET USER BY ID
# def get_user_by_id(user_id: int, db: Session):
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# # UPDATE USER
# def update_user(user_id: int, data, db: Session):
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     user.name = data.name
#     user.email = data.email
#     user.password = hash_password(data.password)
#     db.commit()
#     db.refresh(user)
#     return {
#         "message": "User updated successfully.",
#         "user_id": user.id
#     }


# # DELETE USER
# def delete_user(user_id: int, db: Session):
#     user = db.query(User).filter(User.id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     db.delete(user)
#     db.commit()
#     return {
#         "message": "User deleted successfully.",
#         "user_id": user.id
#     }

