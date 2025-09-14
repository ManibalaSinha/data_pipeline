# worker/Dockerfile
FROM python:3.11-slim
# Install Postgres client so pg_isready works
RUN apt-get update && apt-get install -y postgresql-client

WORKDIR /app

# copy requirements from parent folder
COPY ./api/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt
COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
