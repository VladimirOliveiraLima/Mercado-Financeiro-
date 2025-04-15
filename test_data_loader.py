import pytest
import pandas as pd
from src.trade.data_loader import DataLoader

def test_fetch_data_shape():
    loader = DataLoader()
    df = loader.fetch_data(symbol="AAPL", start="2022-01-01", end="2022-01-10")
    assert isinstance(df, pd.DataFrame)
    assert "Close" in df.columns
    assert "Symbol" in df.columns
    assert len(df) > 0  # Deve ter linhas
