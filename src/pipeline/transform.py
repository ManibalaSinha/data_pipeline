import pandas as pd
import sqlite3

def transform(df):
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Convert columns
    df['amount'] = df['amount'].astype(float)
    df['date'] = pd.to_datetime(df['date'])
    
    # Example: categorize transactions
    df['category'] = df['description'].apply(
        lambda x: 'utility' if 'water' in x.lower() else 'subscription' if 'subscription' in x.lower() else 'other'
    )
    return df
