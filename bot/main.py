import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio
from database.db import Base, engine
from database import models
from telegram_utils import start_client, client
from  scheduler import agendar_rotina

def init_db():
    Base.metadata.create_all(bind=engine)

async def main():
    init_db()
    print("Banco de dados inicializado com sucesso!")

    await start_client()  # inicia o bot e escuta mensagens


if __name__ == "__main__":
    agendar_rotina(30)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_client())
    client.run_until_disconnected()
