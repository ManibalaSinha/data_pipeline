from pipeline.storage import get_conn
from .database import SessionLocal

# Example: return DB connection (used in FastAPI dependency injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

