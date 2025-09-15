import pandas as pd
import sqlite3

def load_to_db(df: pd.DataFrame, conn: sqlite3.Connection) -> None:
    # Ensure the table exists with correct columns
    conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY,
            description TEXT,
            amount REAL,
            date TEXT,
            category TEXT,
            customer_id INTEGER
        )
    """)
    conn.commit()  # commit table creation

    # Insert data
    df.to_sql('transactions', conn, if_exists='append', index=False)
