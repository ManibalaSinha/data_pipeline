import pandas as pd

def extract_csv(file_name: str, raw_path: str) -> pd.DataFrame:
    file_path = f"{raw_path}/{file_name}"
    df = pd.read_csv(file_path)
    return df
