from datetime import timedelta, datetime
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "A3e2d5da"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_token(contact: dict, expire_delta: Optional[timedelta] = None):
    to_encode = contact.copy()
    expire = datetime.utcnow() + (expire_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
