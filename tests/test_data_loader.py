import pandas as pd
import pytest
from src.data_loader.csv_loader import CSVLoader

@pytest.fixture
def dummy_csv(tmp_path):
    path = tmp_path / "dummy.csv"
    pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}).to_csv(path, index=False)
    return path

def test_csv_loader(dummy_csv):
    loader = CSVLoader()
    data = loader.load_data(dummy_csv)
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (3, 2)
