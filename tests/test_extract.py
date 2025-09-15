import os
import pytest
import pandas as pd
from pipeline.extract import extract_csv
from config_loader import load_config

config = load_config()

def test_extract_csv():
    raw_path = config['paths']['raw_data']
    file_path = os.path.join(raw_path, "sample.csv")
    df = extract_csv("sample.csv", raw_path)
    assert len(df) == 5
    assert "amount" in df.columns