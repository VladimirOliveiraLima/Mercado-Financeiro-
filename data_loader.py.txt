import pandas as pd
import numpy as np
import requests
from datetime import datetime

class DataLoader:
    """
    Classe para carregar dados de mercado.
    Pode ser adaptada para fontes distintas (APIs, CSV, BD, etc.)
    """

    def __init__(self, source="MockAPI"):
        self.source = source

    def fetch_data(self, symbol: str, start: str, end: str) -> pd.DataFrame:
        """
        Busca dados para um símbolo (ex: AAPL) entre duas datas.
        """
        # Exemplo simples usando dados fictícios ou API mockada
        # Aqui, para fins de demonstração, geramos dados sintéticos.

        # Caso real: usar requests para API real
        # response = requests.get("URL_DA_API", params={"symbol": symbol, "start": start, "end": end})
        # data = response.json()

        # Para o exemplo, vamos simular datas e preços
        dates = pd.date_range(start=start, end=end, freq='D')
        data = pd.DataFrame(index=dates)
        data["Close"] = np.random.uniform(100, 200, len(dates))  # preços entre 100 e 200
        data["Symbol"] = symbol

        # Ajuste final
        data.index.name = "Date"

        return data
