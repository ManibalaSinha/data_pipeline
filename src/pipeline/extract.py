import pandas as pd
import os

def extract_csv(file_name, raw_path):
    file_path = os.path.join(raw_path, file_name)
    df = pd.read_csv(file_path)
    return df
