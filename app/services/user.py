from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate


def register_user(user: UserCreate, db: Session):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(id: str, db: Session):
    result = db.query(User).filter(User.uid == id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result

def update_user(id: str, user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.uid == id).first()
    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    for key, value in user.model_dump(exclude={"uid"}).items():
        setattr(db_user, key,value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(id: str, db: Session):

    db_query = db.query(User).filter(User.uid == id).delete()
    if db_query == 0:
        raise HTTPException(status_code=404, detail="User not found")
    db.commit()
    return {
        "message": "User deleted successfully",
        "status": 200
    }
