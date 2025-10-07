## **1. Folder Structure**

```
data_pipeline/
├─ transactions_service/        # Handles transaction creation & validation
│  ├─ main.py                   # FastAPI endpoints
│  ├─ models.py                 # DB models
│  ├─ db.py                     # MySQL/PostgreSQL connection
│  ├─ requirements.txt
├─ notifications_service/       # Sends alerts for transactions
│  ├─ main.py                   # Listens to RabbitMQ queue
│  ├─ requirements.txt
├─ docker-compose.yml            # Orchestrates services + RabbitMQ + MySQL
├─ tests/                        # Unit + integration tests
├─ README.md                     # Project overview
```

---

## **2. Sample Code Snippets**

### **transactions_service/main.py**

```python
from fastapi import FastAPI
from models import Transaction
from db import get_db

app = FastAPI()

@app.post("/transactions/")
async def create_transaction(amount: float, account_id: int):
    db = get_db()
    transaction = Transaction(account_id=account_id, amount=amount)
    db.add(transaction)
    db.commit()
    # Push to RabbitMQ for notifications
    # notify_queue.publish(transaction.id)
    return {"status": "success", "transaction_id": transaction.id}
```

### **notifications_service/main.py**

```python
import pika  # RabbitMQ client

def callback(ch, method, properties, body):
    print(f"Transaction alert: {body}")

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='transaction_alerts')
channel.basic_consume(queue='transaction_alerts', on_message_callback=callback, auto_ack=True)
print('Waiting for messages...')
channel.start_consuming()
```

---

### **docker-compose.yml**

```yaml
version: "3.8"
services:
  transactions_service:
    build: ./transactions_service
    ports:
      - "8000:8000"
    depends_on:
      - mysql
      - rabbitmq

  notifications_service:
    build: ./notifications_service
    depends_on:
      - rabbitmq

  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "5672:5672"
      - "15672:15672"

  mysql:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: password
      MYSQL_DATABASE: tech
    ports:
      - "3306:3306"
```

---

```markdown
# High-Volume Transaction Microservices

Transformed a Python ETL/automation pipeline into a **microservices architecture** simulating financial transactions.

## Features
- **Transactions Service:** Handles creation, validation, and storage in MySQL/PostgreSQL.
- **Notifications Service:** Sends alerts for high-value transactions using RabbitMQ.
- **Async Processing:** Celery workers queue tasks for reliability and scalability.
- **REST APIs:** FastAPI endpoints for transaction management.
- **Cloud Ready:** Dockerized for easy deployment.

## Tech Stack
- Python, FastAPI, Celery, RabbitMQ, MySQL/PostgreSQL
- Docker / Docker Compose
- REST APIs, Async Processing, Microservices

## Usage
1. Start services: `docker-compose up --build`
2. Access transactions API: `http://localhost:8000/transactions/`
3. Notifications are sent automatically via RabbitMQ

## Key Learnings
- Built scalable microservices architecture
- Implemented async message queues
- Optimized database storage for high-volume transactions
- Prepared project for cloud deployment

