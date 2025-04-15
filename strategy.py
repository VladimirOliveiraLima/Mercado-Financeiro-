import pandas as pd

class SimpleMovingAverageStrategy:
    """
    Exemplo de estratégia de SMA (Short e Long).
    Gera sinal de compra quando a média curta cruza acima da média longa,
    e sinal de venda quando a média curta cruza abaixo da média longa.
    """

    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Retorna um DataFrame com colunas de sinais (Signal).
        Sinal +1 = Compra, 0 = Nada, -1 = Venda
        """
        df = data.copy()
        df["SMA_Short"] = df["Close"].rolling(window=self.short_window).mean()
        df["SMA_Long"] = df["Close"].rolling(window=self.long_window).mean()

        df["Signal"] = 0
        df["Signal"] = df.apply(self._calculate_signal, axis=1)
        return df

    def _calculate_signal(self, row):
        if pd.isna(row["SMA_Short"]) or pd.isna(row["SMA_Long"]):
            return 0
        elif row["SMA_Short"] > row["SMA_Long"]:
            return 1
        elif row["SMA_Short"] < row["SMA_Long"]:
            return -1
        else:
            return 0
