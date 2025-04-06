import re
from datetime import datetime

def parse_signal_message(message: str):
    padrao = {
        'ativo': r'Ativo:\s*(.+)',
        'entrada': r'Horário da Entrada:\s*(\d{2}:\d{2})',
        'ordem': r'Ordem:\s*(\w+)',
        'reentrada1': r'1ª REENTRADA\s*—>\s*(\d{2}:\d{2})',
        'reentrada2': r'2ª REENTRADA\s*—>\s*(\d{2}:\d{2})',
    }
    
    resultado = {}
    for chave, regex in padrao.items():
        match = re.search(regex, message)
        resultado[chave] = match.group(1) if match else None

    hoje = datetime.now()
    for key in ['entrada', 'reentrada1', 'reentrada2']:
        if resultado[key]:
            hora, minuto = map(int, resultado[key].split(':'))
            resultado[key] = hoje.replace(hour=hora, minute=minuto, second=0, microsecond=0)
        else:
            resultado[key] = None

    return resultado

