def formata_float_str_moeda(valor: float) -> str:
    """Na programação precisamos usar o '.' como separador de campos decimais
       entretando a moeda brasileira Real usa a vírgula como esse separador, por isso
       essa função realiza essa formatação."""
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')