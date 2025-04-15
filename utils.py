def calculate_drawdown(equity_curve):
    """
    Exemplo de função para calcular drawdown máximo.
    Recebe uma lista ou Series com valores do portfólio ao longo do tempo.
    Retorna o drawdown máximo (em valor ou %).
    """
    max_val = 0
    max_drawdown = 0

    for value in equity_curve:
        if value > max_val:
            max_val = value
        drawdown = (max_val - value)
        if drawdown > max_drawdown:
            max_drawdown = drawdown

    return max_drawdown

def format_currency(value):
    """
    Formata valores numéricos como moeda, por exemplo: 12345.67 => "R$ 12.345,67"
    (Apenas um exemplo simplificado. Pode ser customizado para locale.)
    """
    return f"R$ {value:,.2f}"
