import os
import pandas as pd
from pipeline.transform import transform

def test_transform_basic():
    # Create a sample DataFrame (temporary, no external CSV needed)
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "description": ["Water Bill", "Netflix Subscription", "Electricity"],
        "amount": ["50.5", "15.0", "75.25"],  # as strings to test transform
        "date": ["2025-09-01", "2025-09-02", "2025-09-03"]
    })

    # Call the transform function
    df_transformed = transform(df)

    # Assertions
    assert df_transformed['amount'].dtype == float
    assert pd.api.types.is_datetime64_any_dtype(df_transformed['date'])
    assert "category" in df_transformed.columns
    assert df_transformed['category'].tolist() == ['utility', 'subscription', 'other']
