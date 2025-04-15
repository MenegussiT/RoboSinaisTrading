import os
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
session_name = os.getenv("TELEGRAM_SESSION_NAME", "robo_sinais")

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    print("📋 Chats encontrados:\n")
    async for dialog in client.iter_dialogs():
        tipo = "Grupo" if dialog.is_group else "Canal" if dialog.is_channel else "Privado"
        print(f"{dialog.name} ({tipo}) — ID: {dialog.id}")
    
    
    if "Mai Trader - Free" in dialog.name:
        print(f"{dialog.name} — ID: {dialog.id}")


with client:
    client.loop.run_until_complete(main())

