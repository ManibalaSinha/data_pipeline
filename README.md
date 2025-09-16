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

# Data Pipeline

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


