#  Data Pipeline — Microservices-Based Transaction Processing System

**Data Pipeline** is a **scalable, event-driven microservices system** built using **FastAPI, RabbitMQ, and Celery**, with a **Next.js dashboard** for real-time visibility.

Originally designed as a Python ETL workflow, it was re-architected into a **distributed system** capable of handling **high-volume transactions, asynchronous processing, and real-time monitoring**.

---

##  Problem Statement

Traditional ETL pipelines:

* Struggle with **scalability under high load**
* Lack **real-time observability**
* Are tightly coupled and hard to extend

**This project solves these by introducing microservices, async queues, and a monitoring dashboard.**

---

##  Core Features

###  Transaction Processing Service

* `POST /transactions/` → Create and validate transactions
* Ensures **data integrity** with relational databases (MySQL/PostgreSQL)
* Designed for **high-throughput ingestion**

---

###  Notification Service (Event-Driven)

* Listens to RabbitMQ queues
* Sends alerts for **high-value or critical transactions**
* Decoupled from core processing for scalability

---

###  Asynchronous Task Processing

* **Celery workers** handle background jobs
* Enables:

  * Retry handling
  * Non-blocking processing
  * Fault tolerance

---

###  Real-Time Dashboard (Next.js)

* Displays:

  * Transaction status
  * Pipeline activity
  * System metrics
* Built with **server-side rendering (SSR)** for performance

---

##  System Architecture

```id="sys7dp"
Client (Next.js Dashboard)
          │
          ▼
   API Gateway (FastAPI)
          │
          ▼
Transactions Service ───────► Database (PostgreSQL/MySQL)
          │
          ▼
Message Queue (RabbitMQ)
          │
          ▼
Notifications Service (Consumers)
          │
          ▼
     Alerts / Logs
```

---

##  Key Engineering Highlights

* Designed **loosely coupled microservices** for independent scaling
* Implemented **event-driven communication** using RabbitMQ
* Built **async processing pipeline** with Celery workers
* Ensured **data consistency and validation** at service level
* Reduced system blocking by offloading heavy tasks to queues
* Created **real-time observability layer** via frontend dashboard

---

##  Tech Stack

* **Frontend:** Next.js, React
* **Backend:** Python, FastAPI
* **Async Processing:** Celery
* **Messaging:** RabbitMQ
* **Database:** MySQL / PostgreSQL
* **DevOps:** Docker, Docker Compose

---

##  Project Structure

```id="str9dp"
data_pipeline/
├── transactions_service/     # Handles transaction creation & validation
│   ├── main.py               # FastAPI endpoints
│   ├── models.py             # DB models
│   ├── db.py                 # Database connection
│
├── notifications_service/    # Event-driven consumer (RabbitMQ)
│   ├── main.py
│
├── frontend/                 # Next.js dashboard
│
├── docker-compose.yml        # Service orchestration
├── tests/                    # Unit & integration tests
└── README.md
```

---

##  Getting Started

### 1. Start backend services

```bash
docker-compose up --build
```

### 2. Run frontend

```bash
cd frontend
npm install
npm run dev
```

### 3. Access dashboard

```
http://localhost:3000
```

---

##  API Example

### Create Transaction

```bash
POST /transactions/
```

```json
{
  "account_id": 1,
  "amount": 500
}
```

### Response

```json
{
  "status": "success",
  "transaction_id": 123
}
```

---

##  Scalability & Performance

* Handles **high-volume transaction ingestion** using async queues
* Supports **horizontal scaling** of services independently
* Reduces API latency by offloading heavy tasks to background workers
* Designed for **event-driven cloud architectures**

---

##  Future Enhancements

* Distributed tracing (OpenTelemetry)
* Rate limiting & API throttling
* Kafka / PubSub for large-scale streaming
* Role-based access & authentication
* Advanced monitoring (Prometheus + Grafana)

---

##  Why This Project Stands Out

This project demonstrates:

* Real-world **microservices architecture design**
* Strong understanding of **event-driven systems**
* Experience with **async processing and queues**
* Ability to build **end-to-end systems (backend + frontend)**

 Not just ETL — **a scalable distributed system with real-time visibility**

---

##  Author

**Manibala Sinha**
Senior Backend Engineer | Python | FastAPI

GitHub: [https://github.com/ManibalaSinha](https://github.com/ManibalaSinha)

---

Key Highlights:
Next.js Frontend: Built a dashboard to display pipeline jobs, metrics, and transaction status using server-side rendering.

Backend Microservices:
Transactions Service: Handles creation, validation, and storage in MySQL/PostgreSQL.
Notifications Service: Sends alerts via RabbitMQ for high-value transactions.
Async Processing & Queues: Celery workers and RabbitMQ for reliable, scalable task handling.
API Design: FastAPI endpoints for transactions and metrics.
Dockerized & Cloud-Ready: Services orchestrated via Docker Compose for easy deployment.
Tech Stack: Next.js, React, Python, FastAPI, Celery, RabbitMQ, MySQL/PostgreSQL, Docker, Docker Compose, REST APIs, Microservices

Usage / Demo:
Start backend services: docker-compose up --build
Run Next.js frontend: cd frontend && npm run dev
Access dashboard: http://localhost:3000
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



