# JWT auth, password hashing

from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from app.core.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


#Hash password
def hash_password(password: str):
    # bcrypt limit fix
    password = password[:72]
    return pwd_context.hash(password)


#verify password
def verify_password(plain, hashed):
    plain = plain[:72]
    return pwd_context.verify(plain, hashed)


#create access token
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


# #decode access token
# def decode_access_token(token: str):
#     return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

