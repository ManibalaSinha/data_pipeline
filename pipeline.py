#Core ETL Logic
import requests
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)

def fetch_data():
   logging.info("Fetching data from API...")
   response = requests.get("http://localhost:8000/users.json")
   response.raise_for_status()
   return response.json()
def transform_data(data):
   logging.info("Transforming data...")
   for item in data:
      if item.get("status")=="active":
         yield{
            "id": item["id"],
            "name": item["name"],
            "email": item["email"]
         }
def load_data(records):
   logging.info("Loading data into PostgreSQL...")
   conn = psycopg2.connect(database="db", user="postgres", password="password", host="localhost")
   cur = conn.cursor()
   for record in records:
      cur.execute(
         "insert into users(id, name, email) values(%s,%s,%s)on conflict(id)do update set name= excluded.name,email=excluded.email",(record["id"], record["name"], record["email"])
      )
      conn.commit()
      conn.close()
      logging.info("Data loaded successfully!")
def run_pipeline():
   data = fetch_data()
   transform =transform_data(data)
   load_data(transformed)
if __name__ == "__main__":
   run_pipeline()