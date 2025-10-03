from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from starlette import status

from app.database.session import get_db
from app.models.user import User
from app.security.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")


def current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Count not validate",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_token(token)
        username = payload.get(
            "data")  # because data is defined in payload view payload you will see variable->data from it we are getting username
        user = db.query(User).filter(User.contact == username).first()
        if user is None:
            raise credential_exception
        return user
    except JWTError:
        raise credential_exception
