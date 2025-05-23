from .. import schemas, models 
from sqlalchemy.orm import Session
from typing import Annotated
from ..security import security

def create(request: Annotated[str, schemas.User], db: Session):
    new_user = models.User(username = request.username, email = request.email, password = security.get_hashed_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db: Session):
    users = db.query(models.User).all()
    return users

