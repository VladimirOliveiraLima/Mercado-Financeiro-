import sys
from src.trade.data_loader import DataLoader
from src.trade.strategy import SimpleMovingAverageStrategy
from src.trade.trader import Trader

def main():
    print("=== Iniciando Trade-Financial-Market ===")

    # Etapa 1: Carregar dados
    data_loader = DataLoader()
    market_data = data_loader.fetch_data(symbol="AAPL", start="2022-01-01", end="2022-12-31")
    print("Dados carregados com sucesso.")

    # Etapa 2: Definir estratégia
    strategy = SimpleMovingAverageStrategy(short_window=20, long_window=50)

    # Etapa 3: Executar o backtest
    signals = strategy.generate_signals(market_data)
    print("Sinais gerados pela estratégia.")

    # Etapa 4: Realizar trades (exemplo de execução simples)
    trader = Trader(capital=100000.0)
    final_portfolio_value = trader.execute_trades(market_data, signals)
    print(f"Valor final do portfólio: ${final_portfolio_value:.2f}")

    print("=== Fim do processo de trading ===")


if __name__ == "__main__":
    sys.exit(main())
