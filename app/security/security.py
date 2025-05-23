from passlib.context import CryptContext
from sqlalchemy.orm import Session
from .. import models
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

pwd_context = CryptContext(schemes=['bcrypt'])

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_hashed_password(password):
    return pwd_context.hash(password)

