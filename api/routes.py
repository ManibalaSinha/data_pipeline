from fastapi import FastAPI, APIRouter, HTTPException, status, Depends, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy import select, text
from sqlalchemy.orm import Session
from datetime import timedelta

from pipeline.dependencies import get_db
from pipeline.storage import posts, get_conn
from pipeline.auth import (
    authenticate_user,
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from pipeline.schemas import Token, User

app = FastAPI()
router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# ---------- Utility ----------
def write_log(message: str):
    with open("requests.log", "a") as f:
        f.write(message + "\n")


# ---------- Routes ----------
@app.get("/")
def root():
    return {"message": "API is running"}


@router.get("/data")
def get_posts(limit: int = 10, db: Session = Depends(get_db)):
    stmt = select(posts).limit(limit)
    result = db.execute(stmt)
    rows = result.fetchall()

    return {
        "count": len(rows),
        "data": [dict(row._mapping) for row in rows]  # conversion
    }


@router.get("/status")
def status_check():
    try:
        with get_conn() as conn:
            conn.execute(text("SELECT 1"))
        return {"db": "ok"}
    except Exception:
        raise HTTPException(status_code=500, detail="db-connection-failed")


@router.get("/background")
def background_example(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Background task executed")
    return {"message": "Task scheduled"}


# SINGLE login endpoint (clean)
@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": user["username"]},  # or user.username
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/protected", response_model=User)
def protected_route(current_user: User = Depends(get_current_user)):
    return current_user


#  include router
app.include_router(router)
