from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.security.dependencies import oauth2_scheme
from app.security.security import create_token

authentication = APIRouter(
    prefix="/api",
    tags=["Auth Management"]
)


@authentication.post("/auth/token")
def login_for_access_token(data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.contact == data.username).first()
    return {

        "access_token": create_token(contact={"data": db_user.contact}),
        "token_type": "bearer",
        "status": 200
    }
