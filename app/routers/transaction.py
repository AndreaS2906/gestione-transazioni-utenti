from fastapi import APIRouter, Depends, Form, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas
from ..security import security, token, oauth2
from ..database import get_db
from ..repository import user, transaction
from typing import List, Annotated
from datetime import timedelta

router = APIRouter(
    prefix='/transactions',
    tags=['Transactions']
)

@router.post('/add', response_model=schemas.TransactionCreate)
def add_transaction(new_transaction: Annotated[schemas.TransactionCreate, Form()], current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], db: Annotated[Session, Depends(get_db)]):
    return transaction.add_transaction(new_transaction, db, current_user)

@router.get('/get', response_model=List[schemas.Transaction])
def get_all_transactions(current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], db: Annotated[Session, Depends(get_db)]):
    return transaction.get_all_transactions(current_user, db)

@router.post('/update', response_model=schemas.Transaction)
def update_transaction(id: int, update: Annotated[schemas.TransactionCreate, Depends()], current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], db: Annotated[Session, Depends(get_db)]):
    return transaction.update_transaction(id, update, current_user, db)

@router.delete('/delete', response_model=schemas.Transaction)
def delete_transaction(id: int, current_user: Annotated[schemas.User, Depends(oauth2.get_current_user)], db: Annotated[Session, Depends(get_db)]):
    return transaction.delete_transaction(id, current_user, db)