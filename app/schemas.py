from pydantic import BaseModel, ConfigDict, field_serializer
from typing import List, Optional
from datetime import datetime
from zoneinfo import ZoneInfo

class User(BaseModel):
    username : str
    email : str 
    password : str
    model_config = ConfigDict(from_attributes=True)
    
class TransactionCreate(BaseModel):
    amount : float
    description : Optional[str] = None 
    model_config = ConfigDict(from_attributes=True)
    
class Transaction(BaseModel):
    id : int 
    amount : float
    resoconto : float
    description : Optional[str] = None 
    data : datetime
    user_id : int
    model_config = ConfigDict(from_attributes=True)

    @field_serializer('data')
    def serialize_data(self, dt: datetime):
        return dt.astimezone(ZoneInfo("Europe/Rome")).strftime('%d/%m/%Y %H:%M:%S')
    
    model_config = ConfigDict(from_attributes=True)
    
class Token(BaseModel):
    access_token: str
    token_type: str
    model_config = ConfigDict(from_attributes=True)
    
class TokenData(BaseModel):
    username: str | None = None
    model_config = ConfigDict(from_attributes=True)