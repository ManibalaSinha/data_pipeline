import pandas as pd
import sqlite3

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()  # avoids SettingWithCopyWarning
    df['amount'] = df['amount'].astype(float)
    df['date'] = pd.to_datetime(df['date'])
    df['category'] = df['description'].apply(
        lambda x: 'utility' if 'water' in x.lower() else
                  'subscription' if 'subscription' in x.lower() else 'other'
    )
    return df

