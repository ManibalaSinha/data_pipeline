import pandas as pd
from pipeline.extract import extract_csv   # import the real function

def test_extract_csv(tmp_path):
    # Create a sample CSV
    csv_file = tmp_path / "sample.csv"
    df = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
    df.to_csv(csv_file, index=False)

    # Calling the real function
    result = extract_csv("sample.csv", str(tmp_path))

    assert not result.empty
    assert list(result.columns) == ["id", "name"]
    assert result.iloc[0]["name"] == "Alice"
