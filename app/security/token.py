from .. import schemas
from datetime import timedelta, datetime
import jwt

SECRET_KEY = 'c5c12703fc34042259dc085518902be76af2660e15cf9703e617fcdc30062e7b'
ALGORITHM = 'HS256'
ACCESS_TOKEN_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes= 15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get('sub')
        if username is None:
            raise credential_exception
        token_data = schemas.TokenData(username=username)
    except:
        raise credential_exception
    return token_data