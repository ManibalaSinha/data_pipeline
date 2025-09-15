import sqlite3
import pandas as pd
from pipeline.load import load_to_db

def test_load_to_db(tmp_path):
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)

    df = pd.DataFrame({
    "transaction_id": [1, 2],
    "description": ["Water Bill", "Internet"],
    "amount": [50.5, 60.0],
    "date": pd.to_datetime(["2025-09-01", "2025-09-02"]),
    "category": ["utility", "utility"]
})


    load_to_db(df, conn)

    result = pd.read_sql("SELECT * FROM transactions", conn)
    assert len(result) == 2
    conn.close()
