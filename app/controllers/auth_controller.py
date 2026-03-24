from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token


# REGISTER USER
def register_user(data, db: Session):
    
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Check if first user (Admin)
    total_users = db.query(User).count()

    user_type = "Admin" if total_users == 0 else "Employee"

    new_user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        type=user_type,
        created_by=0 if total_users == 0 else 1
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": f"{user_type} registered successfully",
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
    