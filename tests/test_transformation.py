# tests/test_transformation.py
import pandas as pd
from modules.transformation import clean_data

def test_clean_data():
    df = pd.DataFrame({"name": ["Alice", None], "age": [25, 30]})
    cleaned = clean_data(df)
    assert cleaned.shape[0] == 1  # row with None should be removed
