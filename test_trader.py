import pytest
import pandas as pd
from src.trade.trader import Trader

def test_execute_trades():
    # Cria DataFrame de teste
    data = pd.DataFrame({
        "Close": [10, 11, 12, 13],
        "Symbol": ["TEST"]*4
    }, index=pd.date_range("2022-01-01", periods=4))

    # Sinais (compra, compra, vende, nada)
    signals = data.copy()
    signals["Signal"] = [1, 1, -1, 0]

    trader = Trader(capital=100.0)
    final_value = trader.execute_trades(data, signals)

    # Apenas checamos se o valor final é numérico (no caso real, validar comportamento exato)
    assert isinstance(final_value, float)
    assert final_value > 0
