from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordBearer

from jose import JWTError
from jose import jwt

from sqlalchemy.orm import Session

from .database import get_db
from .security import SECRET_KEY
from .security import ALGORITHM


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
    )

def get_current_user(

        token: str = Depends(
            oauth2_scheme
        ),

        db: Session = Depends(
            get_db
        )

):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("id")

        if user_id is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

        return user_id

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Could not validate token"
        )