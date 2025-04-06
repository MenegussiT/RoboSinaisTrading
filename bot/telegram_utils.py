# Importando as bibliotecas necessárias
import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()

# Carregando as variáveis de ambiente
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
session_name = os.getenv('TELEGRAM_SESSION_NAME', 'robo_sinais')

client = TelegramClient(session_name, api_id, api_hash)

async def start_client():
    await client.start()
    print("Cliente do Telegram iniciado com sucesso!")

    @client.on(events.NewMessage(chats=[1002439641464])) # ID do grupo de sinais
    async def handler(event):
        message = event.message.message
        # Aqui você pode processar a mensagem recebida
        print(f"Nova mensagem recebida: {message}")


# Iniciando o cliente do Telegram
if __name__ == "__main__":
    import asyncio
    asyncio.run(start_client())
