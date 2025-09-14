from fastapi import APIRouter, HTTPException, status
from pipeline.storage import engine, posts, get_conn
from sqlalchemy import select, text
from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from pipeline.dependencies import get_db
from fastapi import BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta
from pipeline.auth import authenticate_user, create_access_token, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES
from pipeline.schemas import Token, User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app= FastAPI()

def write_log(message: str):
    with open("requests.log", "a") as f:
        f.write(message + "\n")

@app.get("/")
def root():
    return {"message": "API is running "}

@router.get("/data")
async def get_posts(limit: int = 10, db: Session = Depends(get_db)):
    with engine.connect() as conn:
        stmt = select(posts).limit(limit)  # select([posts]) is legacy; just select(posts)
        res = conn.execute(stmt)
        rows = db.execute(stmt).fetchall()
    return {"count": len(rows), "data": [dict(r) for r in rows]}


@router.get("/status")
async def status():
    # simple status check: DB connectivity
    try:
        with get_conn() as conn:
            conn.execute(text("SELECT 1"))
        return {"db": "ok"}
    except Exception:
        raise HTTPException(status_code=500, detail="db-connection-failed")

@router.get("/background")
async def background_example(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, "Background task executed")
    return {"message": "Task scheduled"}

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/secure-data")
async def secure_data(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user['username']}, here is your secure data!"}


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login with username and password.
    Returns a JWT access token if valid.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/protected", response_model=User)
async def protected_route(current_user: User = Depends(get_current_user)):
    """
    Example protected route.
    Requires valid JWT.
    """
    return current_user
