import sqlite3
import pandas as pd
from pipeline.load import load_to_db

def test_load_to_db(tmp_path):
    # Create a temporary database
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(db_path)

    # Sample DataFrame
    df = pd.DataFrame({
        "transaction_id": [1, 2],
        "description": ["Water Bill", "Internet"],
        "amount": [50.5, 60.0],
        "date": pd.to_datetime(["2025-09-01", "2025-09-02"]),
        "category": ["utility", "utility"]
    })

    # Call load function
    load_to_db(df, conn)

    # Check database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    assert len(rows) == 2

    conn.close()
