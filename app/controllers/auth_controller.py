from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.models.role import Role
from app.models.user_role import UserRole
from app.models.employee import Employee
from app.core.security import hash_password, verify_password, create_access_token


def register_user(data, db: Session):
    #check duplicate email
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists.")
    
    #check total users
    total_users = db.query(User).count()

    #first user ->  admin
    if total_users == 0:
        admin_role = db.query(Role).filter(Role.name == 'admin').first()

        if not admin_role:
            raise HTTPException(status_code=500, detail="Admin role not found.")
        
        user_type = 'admin'
        created_by = 0
    else:
        user_type = 'employee'
        # created_by = 1

        # 🔥 get admin dynamically
        admin_user = db.query(User).filter(User.type == 'admin').first()
        
        if not admin_user:
            raise HTTPException(status_code=500, detail="Admin user not found.")

        created_by = admin_user.id
        # created_by = admin_user.id if admin_user else 1

    
    #create user
    new_user = User(
        name = data.name,
        email = data.email,
        password = hash_password(data.password),
        type = user_type,
        created_by = created_by

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    

    if total_users == 0:
        role_id = admin_role.id

    else:
        default_role = db.query(Role).filter(Role.name == 'employee').first()
        if not default_role:
            raise HTTPException(status_code=500, detail="Default Employee Role Not found.")
        role_id = default_role.id

    user_role = UserRole(
        user_id = new_user.id,
        role_id=role_id
    )
    db.add(user_role)
    db.commit()


    # 6. CREATE EMPLOYEE (ONLY NON-ADMIN USERS)
    if total_users != 0:
        employee = Employee(
            user_id=new_user.id,
            name=data.name,
            email=data.email,
            password=new_user.password,
            employee_id=f"EMP{new_user.id}",
            branch_id=1,          # TODO: dynamic later
            department_id=1,      # TODO: dynamic later
            designation_id=1,     # TODO: dynamic later
            created_by=created_by
        )

        db.add(employee)
        db.commit()

    return {
        "message": f"{user_type} registered successfully.",
        "user_id": new_user.id
    }



# LOGIN USER
def login_user(data, db: Session):


    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    # Create JWT Token
    token = create_access_token({"user_id": user.id})

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "type": user.type
        }
    }
    