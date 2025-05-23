from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
from zoneinfo import ZoneInfo

class User(Base):
    __tablename__ = 'User'
    
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True, index=True)
    username = Column(String(10), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255), index=True)
    
    transactions = relationship('Transactions', back_populates='user')
    
class Transactions(Base):
    __tablename__ = 'Transactions'
    
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    resoconto = Column(Float, nullable=True)
    description = Column(String(255), nullable=True)
    data = Column(DateTime, default=lambda: datetime.now(tz=ZoneInfo("Europe/Rome")))
    user_id =Column(Integer, ForeignKey('User.id'))
    
    user = relationship('User', back_populates='transactions')
    