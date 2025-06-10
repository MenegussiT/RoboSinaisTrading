import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
from database.db import Base, engine
from database import models
from bot.telegram_utils import start_client, client # client é necessário para run_until_disconnected
from bot.scheduler import signal_scheduler # Importa a função do agendador

def init_db():
    Base.metadata.create_all(bind=engine)

async def main():
    init_db()
    print("Banco de dados inicializado com sucesso!")

    # Inicia o cliente Telegram e o agendador de sinais concorrentemente
    await asyncio.gather(
        start_client(), # Escuta as mensagens do Telegram
        signal_scheduler() # Processa a fila de sinais e agenda as execuções
    )

if __name__ == "__main__":
    try:
        asyncio.run(main()) # Inicia o loop de eventos e executa a função main
    except KeyboardInterrupt:
        print("⛔ Encerrando o robô manualmente.")
    finally:
        # Adicione aqui qualquer lógica de limpeza necessária ao encerrar
        print("Bot encerrado.")