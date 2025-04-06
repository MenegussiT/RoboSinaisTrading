import asyncio
from database.db import Base, engine
from database import models
from telegram_utils import start_client, client

def init_db():
    Base.metadata.create_all(bind=engine)

async def main():
    init_db()
    print("Banco de dados inicializado com sucesso!")

    await start_client()  # inicia o bot e escuta mensagens


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_client())
    client.run_until_disconnected()
