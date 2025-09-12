from fastapi import FastAPI, BackgroundTasks
from pipeline.config import load_settings
from pipeline.tasks import run_pipeline
from api.routes import router
from pipeline.storage import init_db

settings = load_settings()

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/trigger")
def trigger():
    run_pipeline.delay()
    return {"status": "triggered"}

