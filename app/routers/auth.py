from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas
from ..security import token, oauth2
from ..database import get_db
from ..repository import user
from sqlalchemy.orm import Session
from typing import Annotated

router = APIRouter(
    tags=['Auth']
)


@router.post('/user/login')
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(get_db)]) -> schemas.Token:
    user = oauth2.auth_user(username=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail= 'could not validate credential',
        headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_MINUTES)
    access_token = token.create_access_token(data={'sub': user.username}, expires_delta=access_token_expires)
    return schemas.Token(access_token=access_token, token_type='bearer')