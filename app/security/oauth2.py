from typing import Annotated
from fastapi import Depends, HTTPException, status, Security
from .. import models, schemas
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from . import token as tk
from ..database import get_db
from .security import verify_password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/user/login')

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[Session, Depends(get_db)]):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail= 'could not validate credential',
        headers={'WWW-Authenticate': 'Bearer'},
        )
    token_data = tk.verify_token(token, credential_exception)
    user = db.query(models.User).filter(models.User.username == token_data.username).first()
    if not user:
        raise credential_exception
    return schemas.User.model_validate(user)

def auth_user(username: str, password: str, db: Session):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
