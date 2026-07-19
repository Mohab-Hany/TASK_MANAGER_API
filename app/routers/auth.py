from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import UserRegister
from ..schemas import UserLogin
from ..models import User

from ..security import (
    hash_password,
    verify_password,
    create_access_token
)


router = APIRouter(

    prefix="/auth",

    tags=["Authentication"]

)


#====================
# REGISTER
#====================

@router.post("/register")
def register(

        user: UserRegister,

        db: Session = Depends(
            get_db
        )

):

    email_exists = db.query(
        User
    ).filter(

        User.email == user.email

    ).first()


    if email_exists:

        raise HTTPException(

            status_code=400,

            detail="Email already exists"

        )


    username_exists = db.query(
        User
    ).filter(

        User.username == user.username

    ).first()


    if username_exists:

        raise HTTPException(

            status_code=400,

            detail="Username already exists"

        )


    new_user = User(

        username=user.username,

        email=user.email,

        hashed_password=hash_password(
            user.password
        )

    )


    db.add(new_user)

    db.commit()

    db.refresh(new_user)


    return {

        "message":"User Created Successfully"

    }


#====================
# LOGIN
#====================

@router.post("/login")
def login(

        user: UserLogin,

        db: Session = Depends(
            get_db
        )

):


    db_user = db.query(
        User
    ).filter(

        User.email == user.email

    ).first()


    if not db_user:

        raise HTTPException(

            status_code=401,

            detail="Invalid Email Or Password"

        )


    if not verify_password(

            user.password,

            db_user.hashed_password

    ):

        raise HTTPException(

            status_code=401,

            detail="Invalid Email Or Password"

        )


    access_token = create_access_token(

        data={

            "id":db_user.id,

            "email":db_user.email

        }

    )


    return {

        "access_token":access_token,

        "token_type":"bearer"

    }