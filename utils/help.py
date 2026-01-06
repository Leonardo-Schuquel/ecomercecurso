def format_price(val):
    try:
        # Tenta converter para float, se for None ou '' vira 0 ou falha
        val = float(val) if val else 0
        return f'R$ {val:.2f}'.replace('.', ',')
    except (ValueError, TypeError):
        return f'R$ 0,00'