# Data Pipeline

Simulates payment transaction workflows.
Python, ETL, and database skills.
Cloud-ready and production-style architecture.
Includes logging, testing, and containerization, which are standard in financial services engineering.
---

# ** Folder Structure**

```
data_pipeline/
│
├── README.md
├── requirements.txt
├── Dockerfile
├── airflow_dags/
│   └── etl_pipeline.py
├── notebooks/
│   └── analysis.ipynb
├── src/
│   ├── ingestion.py
│   ├── transformation.py
│   ├── loader.py
│   └── utils.py
├── tests/
│   ├── test_ingestion.py
│   ├── test_transformation.py
│   └── test_loader.py
├── data/
│   ├── raw/
│   └── processed/
└── diagrams/
    └── architecture.png
```

---

# **2️⃣ Sample README.md**

````markdown
# Data Pipeline Project

## Overview
This project demonstrates an end-to-end **data engineering pipeline**, including ingestion, transformation, loading, and analytics. It simulates **batch and streaming data pipelines**, integrates multiple data sources, and can run on **cloud environments like Azure**. 

**Technologies:** Python, PySpark, SQL (PostgreSQL), Kafka, Airflow, Docker, Azure Blob Storage, dbt, Pandas

---

## Architecture

![Data Pipeline Architecture](diagrams/architecture.png)

1. **Ingestion:** Fetch data from APIs, CSV, relational databases, or streaming sources.
2. **Transformation:** Clean, normalize, and enrich data using PySpark/Pandas.
3. **Loading:** Save processed data to PostgreSQL, Azure Blob/ADLS, or other storage.
4. **Orchestration:** Manage ETL workflow with Airflow DAGs.
5. **Analysis & Visualization:** Jupyter notebooks for KPIs, dashboards, and reporting.

---

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/ManibalaSinha/data_pipeline.git
cd data_pipeline
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 3. Run Locally

```bash
python src/ingestion.py
python src/transformation.py
python src/loader.py
```

### 4. Run with Docker

```bash
docker build -t data_pipeline .
docker run -it data_pipeline
```

### 5. Run Airflow DAG

* Copy `airflow_dags/etl_pipeline.py` to your Airflow DAGs folder
* Start Airflow webserver and scheduler
* Trigger `etl_pipeline` DAG via UI or CLI

---

## Key Features

* **Batch & streaming pipelines** with Kafka integration
* **PySpark transformations** for large-scale data
* **Cloud-ready architecture** for Azure Blob / ADLS
* **Dockerized** for portability
* **CI/CD friendly** with modular scripts
* **Unit & integration testing** for quality assurance
* **Metrics tracking & logging**

---

## Sample Metrics

| Metric                 | Value          |
| ---------------------- | -------------- |
| Data processed/day     | 500k rows      |
| Avg pipeline execution | 10 mins        |
| Success rate           | 99.5%          |
| Error handling         | Retries + logs |

---

## Future Improvements

* Add **dbt for modular transformations**
* Integrate **Databricks for cloud Spark jobs**
* Extend **streaming pipelines to real-time dashboards**
* Include **more automated tests** and CI/CD pipeline

---

## Author

**Manibala Sinha**

* [GitHub](https://github.com/ManibalaSinha)
* [LinkedIn](https://linkedin.com/in/manibalasinha)

````

---

# **3️⃣ Sample Airflow DAG (`airflow_dags/etl_pipeline.py`)**

```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.ingestion import run_ingestion
from src.transformation import run_transformation
from src.loader import run_loader

default_args = {
    'owner': 'manibala',
    'depends_on_past': False,
    'start_date': datetime(2025, 9, 18),
    'retries': 1,
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='End-to-end ETL pipeline',
    schedule_interval='@daily',
)

ingest_task = PythonOperator(
    task_id='ingest_data',
    python_callable=run_ingestion,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=run_transformation,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=run_loader,
    dag=dag,
)

ingest_task >> transform_task >> load_task
````

---

# **4️⃣ Testing (`tests/test_transformation.py`) Example**

```python
import pandas as pd
from src.transformation import transform_data

def test_transform_data():
    df = pd.DataFrame({'value': [1, 2, None, 4]})
    df_transformed = transform_data(df)
    assert df_transformed['value'].isnull().sum() == 0
``

Folder Structure
data_pipeline/
├── README.md
├── requirements.txt
├── config/
│   ├── config.yaml          # Pipeline and DB configuration
│   └── logging_config.yaml  # Logging settings
├── data/
│   ├── raw/                 # Original raw CSV files
│   ├── processed/           # Cleaned / transformed data
│   └── output/              # Final outputs / reports
├── notebooks/
│   └── summary.ipynb        # Analysis / visualization
├── src/
│   ├── main.py              # Entry point
│   ├── config_loader.py
│   ├── pipeline/            # ETL modules
│   └── utils/               # Logging, DB connectors, helpers
├── tests/                   # Unit tests for pipeline modules
└── docker/                  # Dockerfile & docker-compose
Features
Modular ETL Pipeline

extract.py: Read CSV or API data.

transform.py: Clean, format, and categorize transactions.

load.py: Store data in database (SQLite / Postgres).

Config Management

YAML configuration files to manage paths, database connections, and logging.

Logging

Centralized logger for monitoring pipeline execution.

Unit Testing

Tests for each ETL module using pytest.

Dockerized

Containerized for portability and cloud deployment readiness.

Data Visualization

Jupyter Notebook for summary reports and insights.

Installation
Clone the repo

git clone https://github.com/manibalasinha/data_pipeline.git
cd data_pipeline

Create virtual environment

python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

Install dependencies

pip install -r requirements.txt

Run the pipeline

python src/main.py

A production-like data pipeline demonstrating Python, Celery, FastAPI, PostgreSQL, and Redis. Ideal for backend development, asynchronous task processing, and API design portfolios.

---

##  Quickstart (Local Development)

### Prerequisites

* Docker & Docker Compose
* Python 3.10+ (for local development or testing)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ManibalaSinha/data_pipeline.git
   cd data_pipeline
   ```

2. Build and start the containers:

   ```bash
   docker-compose up --build
   ```

3. Initialize the PostgreSQL database:

   ```bash
   docker exec -it data_pipeline-api-1 python -c "from pipeline.storage import init_db; init_db()"
   ```

4. Access the FastAPI application:

   * Open your browser and navigate to: [http://localhost:8000](http://localhost:8000)
   * API documentation is available at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

##  Project Structure

* `api/`: FastAPI application and routing logic
* `worker/`: Celery worker for asynchronous task processing
* `pipeline/`: Core pipeline logic and database models
* `scripts/`: Utility scripts for data processing and management
* `tests/`: Unit and integration tests
* `Dockerfile`: Docker configuration for the FastAPI application
* `docker-compose.yml`: Docker Compose configuration for multi-container setup
* `requirements.txt`: Python dependencies

---

##  Technologies Used

* **Python 3.10+**: Core programming language
* **FastAPI**: Modern web framework for building APIs
* **Celery**: Asynchronous task queue/job queue based on distributed message passing
* **PostgreSQL**: Relational database management system
* **Redis**: In-memory data structure store, used as a message broker for Celery
* **Docker & Docker Compose**: Containerization and orchestration of services

---

##  Testing

Unit and integration tests are located in the `tests/` directory. To run the tests:

```bash
pytest tests/
```

---

##  API Endpoints

* **GET** `/items/`: Retrieve a list of items
* **POST** `/items/`: Create a new item
* **GET** `/items/{item_id}/`: Retrieve a specific item by ID
* **PUT** `/items/{item_id}/`: Update a specific item by ID
* **DELETE** `/items/{item_id}/`: Delete a specific item by ID

---

##  Cron Jobs

A cron job is set up to run tasks at scheduled intervals. The cron job configuration is located in `cron_job.sh` and is executed within the Docker container.

---

##  Deployment

For deploying to production environments, consider using platforms like AWS, Azure, or Heroku. Ensure that environment variables and production configurations are properly set up.

---

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

##  Contact

For questions or feedback, please reach out to [smanibala.it@gmail.com](mailto:smanibala.it@gmail.com).




