import pandas as pd
from pipeline.transform import transform

def test_transform_basic():
    df = pd.DataFrame({
        "id": [1, 2],
        "description": ["Water", "Internet"],
        "amount": [100, 200],
        "date": pd.to_datetime(["2025-09-01", "2025-09-02"]),
        "category": ["utility", "utility"]
    })

    result = transform(df)
    assert not result.empty
    assert "amount" in result.columns
