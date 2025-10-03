from typing import List

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from fastapi import APIRouter, Depends, HTTPException
from app.services.user import register_user as register
from app.services.user import get_all_users as getalluser
from app.services.user import get_user_by_id as getuserbyid
from app.services.user import update_user as updateuser
from app.services.user import delete_user as deleteuser

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("/create", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = register(user, db)
    return db_user


@router.get("/all", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return getalluser(db)


@router.get("/{id}", response_model=UserResponse)
def get_user_by_id(id: str, db: Session = Depends(get_db)):
    return getuserbyid(id, db)


@router.put("/{id}")
def update_user(id: str, user: UserCreate, db: Session = Depends(get_db)):
    return updateuser(id, user, db)

@router.delete("/{id}")
def delete_user(id: str, db: Session = Depends(get_db)):
    return deleteuser(id, db)
