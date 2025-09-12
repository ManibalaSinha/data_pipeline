import requests
from tenacity import retry, stop_after_attempt, wait_exponential
from pipeline.config import load_settings  # separate import line

settings = load_settings()
BASE = settings['api']['base_url']

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=10))
def fetch_posts():
    url = f"{BASE}{settings['api']['endpoints']['posts']}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()  # properly indented

if __name__ == '__main__':
    data = fetch_posts()
    print(f"fetched {len(data)} items")
