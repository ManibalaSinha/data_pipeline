from sqlalchemy.orm import sessionmaker, session
from pipeline.storage import engine
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pipeline.storage import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    db: Session = next(get_db())
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Dummy placeholder: replace with actual JWT decoding logic
    if token != "fake-token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return {"username": "test_user"}
