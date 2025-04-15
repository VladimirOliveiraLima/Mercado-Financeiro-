import pytest
import pandas as pd
from src.trade.strategy import SimpleMovingAverageStrategy

def test_generate_signals():
    # Cria DataFrame de teste
    data = pd.DataFrame({
        "Close": [10, 11, 12, 13, 14, 15],
        "Symbol": ["TEST"]*6
    })

    strategy = SimpleMovingAverageStrategy(short_window=2, long_window=3)
    signals_df = strategy.generate_signals(data)

    assert "Signal" in signals_df.columns
    assert len(signals_df) == 6
