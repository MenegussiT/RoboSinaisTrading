# bot/telegram_utils.py

import os
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient, events
from datetime import datetime
from bot.message_parser import parse_signal_message
from bot.scheduler import add_signal_to_queue # Certifique-se que essa importação existe

load_dotenv()

api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
session_name = os.getenv("TELEGRAM_SESSION_NAME", "robo_sinais")
GROUP_ID_TEMP = int(os.getenv("TELEGRAM_GROUP_ID_TEMP"))

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.chat_id != GROUP_ID_TEMP:
        return

    mensagem = event.message.message
    print(f"📥 Mensagem recebida:\n{mensagem}\n")

    dados = parse_signal_message(mensagem)
    print("🧩 Dados extraídos:", dados)

    if dados["ativo"] and dados["entrada"]:
        print(f"✅ Sinal válido detectado para {dados['ativo']} às {dados['entrada'].time()}")
        # --- AQUI VAMOS AGENDAR A OPERAÇÃO ---
        await add_signal_to_queue(dados) # Chama a função do scheduler
    else:
        print("⚠️ Mensagem fora do padrão. Ignorada.")

async def start_client():
    print("Iniciando cliente Telegram...")
    await client.start() # Inicia a sessão do cliente Telegram. Essencial para autenticação e conexão.
    print("✅ Cliente Telegram conectado e rodando!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(start_client())