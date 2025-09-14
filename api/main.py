from fastapi import FastAPI, BackgroundTasks, Request
from pipeline import load_settings
from pipeline.tasks import run_pipeline
from api.routes import router
from api.routers import notes
from pipeline.storage import init_db
from api.middleware import LoggingMiddleware
import time

settings = load_settings()

app = FastAPI(title="Data Pipeline API")
app.include_router(notes.router)

app.add_middleware(LoggingMiddleware)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    print(f"Path={request.url.path} took={duration:.4f}s")
    return response

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/")
def root():
    return {"message": "API is running "}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/trigger")
def trigger():
    run_pipeline.delay()
    return {"status": "triggered"}

