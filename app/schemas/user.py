from datetime import datetime

from pydantic import BaseModel, Field



class UserBase(BaseModel):
    uid: str = Field(default=None)
    firstname: str = Field(default=None)
    lastname: str = Field(default=None)
    email: str = Field(default=None)
    contact: str = Field(default=None)
    image: str = Field(default=None)


class UserCreate(UserBase):
    firstname: str = Field(default=None)
    lastname: str = Field(default=None)
    email: str = Field(default=None)
    contact: str = Field(default=None)
    image: str = Field(default=None)

class UserResponse(UserBase):
    createddate: datetime
    updateddate:datetime



