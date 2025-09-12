from fastapi import APIRouter, HTTPException
from pipeline.storage import engine, posts, get_conn
from sqlalchemy import select, text
from fastapi import FastAPI

router = APIRouter()

app= FastAPI()

@app.get("/")
def root():
    return {"message": "API is running "}

@router.get("/data")
async def get_posts(limit: int = 10):
    with engine.connect() as conn:
        stmt = select(posts).limit(limit)  # select([posts]) is legacy; just select(posts)
        res = conn.execute(stmt)
        rows = [dict(r) for r in res]
    return {"count": len(rows), "data": rows}


@router.get("/status")
async def status():
    # simple status check: DB connectivity
    try:
        with get_conn() as conn:
            conn.execute(text("SELECT 1"))
        return {"db": "ok"}
    except Exception:
        raise HTTPException(status_code=500, detail="db-connection-failed")
