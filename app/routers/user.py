from fastapi import APIRouter, Depends, Form, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas
from ..security import security, token, oauth2
from ..database import get_db
from ..repository import user
from typing import List, Annotated
from datetime import timedelta

router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post('/create/', response_model=schemas.User)
def create(request: Annotated[schemas.User, Form()], db: Annotated[Session, Depends(get_db)]):
    return user.create(request, db)

@router.get('/get_all/', response_model=List[schemas.User])
def get_all_users(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], db: Session = Depends(get_db)):
    return user.get_all(db)

