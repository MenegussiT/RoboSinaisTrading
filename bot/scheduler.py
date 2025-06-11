# bot/scheduler.py

import asyncio
from datetime import datetime
from corretora import executar_sinal, logar_corretora, get_browser_page # Importando as funções da corretora

# Fila para armazenar os sinais a serem agendados
signal_queue = asyncio.Queue()

async def add_signal_to_queue(signal_data: dict):
    """Adiciona um sinal à fila de processamento."""
    await signal_queue.put(signal_data)
    print(f"⏰ Sinal para {signal_data['ativo']} às {signal_data['entrada'].time()} adicionado à fila.")

async def signal_scheduler():
    """Monitora a fila de sinais e agenda a execução."""
    # Garante que o navegador está logado uma única vez ao iniciar o scheduler
    await logar_corretora()
    print("🚀 Agendador de sinais iniciado. Aguardando sinais...")

    while True:
        signal_data = await signal_queue.get() # Espera por um novo sinal na fila
        
        horario_entrada = signal_data.get('entrada')
        if not horario_entrada:
            print(f"⚠️ Sinal sem horário de entrada. Ignorando: {signal_data}")
            continue

        now = datetime.now()
        delay_seconds = (horario_entrada - now).total_seconds()

        if delay_seconds > 0:
            print(f"⏳ Agendando execução para {signal_data['ativo']} em {delay_seconds:.2f} segundos.")
            await asyncio.sleep(delay_seconds)
            print(f"🔥 Executando sinal para {signal_data['ativo']} no horário de entrada.")
            await executar_sinal(signal_data) # Chama a função de execução da corretora
        else:
            print(f"⚠️ Horário de entrada para {signal_data['ativo']} já passou. Executando imediatamente.")
            await executar_sinal(signal_data)

        # --- Lógica para Reentradas (Opcional, mas importante) ---
        # Você pode adaptar isso para agendar as reentradas da mesma forma
        reentrada1_time = signal_data.get('reentrada1')
        if reentrada1_time:
            now_reentrada = datetime.now()
            delay_reentrada1 = (reentrada1_time - now_reentrada).total_seconds()
            if delay_reentrada1 > 0:
                print(f"⏳ Agendando 1ª Reentrada para {signal_data['ativo']} em {delay_reentrada1:.2f} segundos.")
                await asyncio.sleep(delay_reentrada1)
                print(f"🔥 Executando 1ª Reentrada para {signal_data['ativo']}.")
                # Aqui você pode ter uma função específica para reentrada ou reusar executar_sinal
                await executar_sinal(signal_data) # Pode ser necessário ajustar 'dados' para a reentrada
            else:
                print(f"⚠️ Horário da 1ª Reentrada para {signal_data['ativo']} já passou.")

        # Lógica semelhante para reentrada2_time se for usada
        reentrada2_time = signal_data.get('reentrada2')
        if reentrada2_time:
            now_reentrada = datetime.now()
            delay_reentrada2 = (reentrada2_time - now_reentrada).total_seconds()
            if delay_reentrada2 > 0:
                print(f"⏳ Agendando 2ª Reentrada para {signal_data['ativo']} em {delay_reentrada2:.2f} segundos.")
                await asyncio.sleep(delay_reentrada2)
                print(f"🔥 Executando 2ª Reentrada para {signal_data['ativo']}.")
                # Aqui você pode ter uma função específica para reentrada ou reusar executar_sinal
                await executar_sinal(signal_data) # Pode ser necessário ajustar 'dados' para a reentrada
            else:
                print(f"⚠️ Horário da 2ª Reentrada para {signal_data['ativo']} já passou.")