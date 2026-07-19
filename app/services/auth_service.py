from sqlalchemy.orm import Session

from ..models import User
from ..security import (
    hash_password,
    verify_password
)


def get_user_by_email(

        email: str,

        db: Session

):

    return db.query(

        User

    ).filter(

        User.email == email

    ).first()


def get_user_by_username(

        username: str,

        db: Session

):

    return db.query(

        User

    ).filter(

        User.username == username

    ).first()


def create_user(

        username: str,

        email: str,

        password: str,

        db: Session

):

    user = User(

        username=username,

        email=email,

        hashed_password=hash_password(
            password
        )

    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def authenticate_user(

        email: str,

        password: str,

        db: Session

):

    user = get_user_by_email(

        email,

        db

    )


    if not user:

        return False


    if not verify_password(

            password,

            user.hashed_password

    ):

        return False


    return user