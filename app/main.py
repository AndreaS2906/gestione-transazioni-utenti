from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db, engine
from . import schemas, models
from .routers import user, auth, transaction
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=engine)
    
    yield
    

app = FastAPI(lifespan=lifespan)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(transaction.router)