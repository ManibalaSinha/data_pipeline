from pipeline.transform import transform

def test_dummy_pipeline():
    in_rec = {"id": 1, "description": "Test", "amount": 10, "date": "2025-09-01", "category": "misc"}
    # Dummy validation – replace with real later
    assert "id" in in_rec
    assert "amount" in in_rec
