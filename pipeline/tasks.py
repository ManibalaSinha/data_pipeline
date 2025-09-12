from celery import Celery
from pipeline.config import load_settings
from pipeline.fetcher import fetch_posts
from pipeline.processor import process_batch
from pipeline.storage import get_conn, upsert_posts

settings = load_settings()

app = Celery(
    'tasks',
    broker=settings['celery']['broker_url'],
    backend=settings['celery']['result_backend']
)

@app.task(bind=True, acks_late=True, max_retries=3)
def run_pipeline(self):
    try:
        raw = fetch_posts()
        batch = process_batch(raw)
        with get_conn() as conn:
            upsert_posts(conn, batch)
        return {'ingested': len(batch)}
    except Exception as exc:
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)

if __name__ == '__main__':
    # local runner for testing
    res = run_pipeline.apply()
    print(res.get())
