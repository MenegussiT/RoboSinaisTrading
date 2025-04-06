# Refatorando erro
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Importando as bibliotecas necessárias
import os
from telethon import TelegramClient, events
from dotenv import load_dotenv
from message_parser import parse_signal_message
from database.db import SessionLocal
from crud.signal import create_signal

load_dotenv()

# Carregando as variáveis de ambiente
api_id = os.getenv("TELEGRAM_API_ID")
api_hash = os.getenv("TELEGRAM_API_HASH")
session_name = os.getenv('TELEGRAM_SESSION_NAME', 'robo_sinais')

client = TelegramClient(session_name, api_id, api_hash)

async def start_client():
    await client.start()
    print("✅ Cliente do Telegram iniciado com sucesso!")

    @client.on(events.NewMessage(chats=[1002439641464]))  # ID do grupo de sinais
    async def handler(event):
        message = event.message.message
        print(f"\n📩 Nova mensagem recebida:\n{message}")

        dados = parse_signal_message(message)
        if dados:
            print(f"✅ Dados extraídos com sucesso:\n{dados}")
            try:
                db = SessionLocal()
                novo_sinal = create_signal(db, dados)
                print(f"💾 Sinal salvo com ID: {novo_sinal.id}")
            except Exception as e:
                print(f"❌ Erro ao salvar no banco: {e}")
            finally:
                db.close()
        else:
            print("⚠️ Mensagem fora do padrão esperado. Ignorada.")
    
        

# Iniciando o cliente do Telegram
if __name__ == "__main__":
    import asyncio
    asyncio.run(start_client())

