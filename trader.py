import pandas as pd

class Trader:
    """
    Classe Trader: gerencia o capital, compra e venda de ativos,
    e calcula valor final do portfólio.
    """

    def __init__(self, capital=10000.0):
        self.initial_capital = capital
        self.positions = {}
        self.cash = capital

    def execute_trades(self, data: pd.DataFrame, signals: pd.DataFrame) -> float:
        """
        Exemplo simples:
        - Quando o sinal é +1, compramos 1 unidade do ativo
        - Quando o sinal é -1, vendemos 1 unidade do ativo
        - Sinal 0 => manter posição
        Retorna valor final do portfólio no final do período.
        """
        symbol = signals["Symbol"].iloc[0] if "Symbol" in signals.columns else "UNDEF"

        for idx, row in signals.iterrows():
            if row["Signal"] == 1:
                # Compra 1 ação
                price = data.loc[idx, "Close"]
                self.cash -= price
                self.positions[symbol] = self.positions.get(symbol, 0) + 1

            elif row["Signal"] == -1:
                # Vende 1 ação (se tiver)
                if self.positions.get(symbol, 0) > 0:
                    price = data.loc[idx, "Close"]
                    self.cash += price
                    self.positions[symbol] -= 1

        final_portfolio_value = self.cash
        # Calcula valor de quaisquer posições remanescentes
        for sym, qty in self.positions.items():
            current_price = data["Close"].iloc[-1]
            final_portfolio_value += qty * current_price

        return final_portfolio_value
