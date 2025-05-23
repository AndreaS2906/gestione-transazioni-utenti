from .. import schemas, models 
from sqlalchemy.orm import Session
from typing import Annotated
from ..security import security
from fastapi import Depends, HTTPException, status
from sqlalchemy import func
from datetime import datetime
from zoneinfo import ZoneInfo


def add_transaction(
    new_transaction: Annotated[schemas.TransactionCreate, Depends()], 
    db: Session, 
    current_user: schemas.User
    ):
    current_user_id = db.query(models.User).filter(models.User.username == current_user.username).first().id
    latest_transaction = db.query(models.Transactions).filter(models.Transactions.user_id == current_user_id).order_by(models.Transactions.id.desc()).first()
    previus_resoconto = latest_transaction.resoconto if latest_transaction else 0
    transaction = models.Transactions(
        amount=new_transaction.amount, 
        resoconto=previus_resoconto+new_transaction.amount,
        description=new_transaction.description, 
        user_id=current_user_id
        )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def get_all_transactions(current_user: schemas.User, db: Session):
    current_user_id = db.query(models.User).filter(models.User.username == current_user.username).first().id
    transactions = db.query(models.Transactions).filter(models.Transactions.user_id == current_user_id).all()
    return transactions

def update_transaction(id: int, update: Annotated[schemas.TransactionCreate, Depends()], current_user: schemas.User, db: Session):
    current_user_id = db.query(models.User).filter(models.User.username == current_user.username).first().id
    transaction = db.query(models.Transactions).filter(models.Transactions.id == id).filter(models.Transactions.user_id == current_user_id).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='any yours transaction with this id')
    total_amount = db.query(func.sum(models.Transactions.amount))\
        .filter(models.Transactions.user_id == current_user_id, models.Transactions.id < id)\
        .scalar() or 0
    current_resoconto = total_amount + update.amount
    db.query(models.Transactions).filter(models.Transactions.id == id, models.Transactions.user_id == current_user_id).update({
        'amount':update.amount,
        'resoconto':current_resoconto,
        'description':update.description,
        'data': datetime.now(tz=ZoneInfo("Europe/Rome"))
        })
    db.commit()
    
    following_transaction = db.query(models.Transactions).filter(models.Transactions.user_id == current_user_id).filter(models.Transactions.id > id).order_by(models.Transactions.id.asc()).all()
    for t in following_transaction:
        current_resoconto += t.amount
        t.resoconto = current_resoconto
    
    db.commit()
    
    return transaction

def delete_transaction(id: int, current_user: schemas.User, db: Session):
    current_user_id = db.query(models.User).filter(models.User.username == current_user.username).first().id
    transaction = db.query(models.Transactions).filter(models.Transactions.id == id).filter(models.Transactions.user_id == current_user_id).first()
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='any yours transaction with this id')
    current_resoconto = transaction.resoconto - transaction.amount
    print(current_resoconto)
    db.delete(transaction)
    db.flush()
    
    following_transaction = db.query(models.Transactions).filter(models.Transactions.user_id == current_user_id).filter(models.Transactions.id > id).order_by(models.Transactions.id.asc()).all()
    for t in following_transaction:
        print(t)
        current_resoconto += t.amount
        t.resoconto = current_resoconto
    db.commit()

    return transaction