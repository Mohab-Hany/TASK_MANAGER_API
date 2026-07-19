from pydantic import BaseModel
from pydantic import EmailStr
from datetime import datetime
from typing import Optional


#========================
# USERS
#========================

class UserRegister(BaseModel):

    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):

    email: EmailStr
    password: str


class UserResponse(BaseModel):

    id: int
    username: str
    email: EmailStr

    class Config:

        from_attributes = True


#========================
# TASKS
#========================

class TaskCreate(BaseModel):

    title: str
    description: str
    priority: str
    deadline: Optional[datetime] = None


class TaskUpdate(BaseModel):

    title: str
    description: str
    priority: str
    deadline: Optional[datetime] = None


class TaskStatus(BaseModel):

    status: bool


class TaskResponse(BaseModel):

    id: int
    title: str
    description: str
    priority: str
    status: bool
    deadline: Optional[datetime]

    class Config:

        from_attributes = True