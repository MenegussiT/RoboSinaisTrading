import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient, events
from datetime import datetime
from bot.message_parser import parse_signal_message



load_dotenv()

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
session_name = os.getenv("TELEGRAM_SESSION_NAME", "robo_sinais")
GROUP_ID = int(os.getenv("TELEGRAM_GROUP_ID", "-1002008142020"))  # Mai Trader Free [ -1002439641464]

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.chat_id != GROUP_ID:
        return  # Ignora outras conversas

    mensagem = event.message.message
    print(f"📥 Mensagem recebida:\n{mensagem}\n")

    dados = parse_signal_message(mensagem)
    print("🧩 Dados extraídos:", dados)

    # Aqui você pode acionar funções específicas para operar o sinal
    if dados["ativo"] and dados["entrada"]:
        print(f"✅ Sinal válido detectado para {dados['ativo']} às {dados['entrada'].time()}")

async def start_client():
    print("✅ Cliente conectado e rodando!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(start_client())
