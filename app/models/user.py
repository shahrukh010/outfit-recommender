from datetime import datetime
import uuid

from sqlalchemy import CHAR, Column, DateTime, String

from app.database.base import Base


class User(Base):
    __tablename__ = 'Users'
    uid = Column(CHAR(45),primary_key=True,default=lambda: str(uuid.uuid4()),nullable=False)
    firstname = Column(String(45),nullable=False)
    lastname = Column(String(45),nullable=False)
    email = Column(String(45),nullable=False,unique=True)
    contact = Column(String(15),nullable=False,unique=True,index=True)
    image = Column(String(255),nullable=True)
    createddate = Column(DateTime,default=datetime.utcnow,nullable=False)
    updateddate = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False)


