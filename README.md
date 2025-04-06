🤖 RoboSinaisTrading
Um robô de trading inteligente que automatiza operações com base em sinais recebidos via Telegram. Desenvolvido com Python, SQLAlchemy e FastAPI.

📌 Funcionalidades
🔍 Leitura de sinais via canal do Telegram

📈 Execução automática de ordens de compra/venda

💰 Gestão de saldo, controle de gains/losses

🗃️ Armazenamento e consulta de sinais em banco de dados

⚙️ APIs REST para criação e leitura de sinais

✅ Testes automatizados com Pytest

🔐 Proteção de chaves de API com variáveis de ambiente

🚀 Tecnologias Utilizadas
Python 3.13

FastAPI

SQLAlchemy

SQLite (modo local)

Pytest

python-telegram-bot (em breve)

Uvicorn

🧪 Testes
Para rodar os testes:

bash
Copiar
Editar
pytest tests/
📁 Estrutura do Projeto
pgsql
Copiar
Editar
📦 RoboSinaisTrading
│
├── app/
│   ├── crud/
│   ├── models.py
│   ├── schemas.py
│   ├── main.py
│   └── database.py
│
├── tests/
│   └── test_crud_signal.py
│
├── .env.example
├── requirements.txt
└── README.md
🔐 Variáveis de Ambiente
Crie um arquivo .env com base no exemplo:

env
Copiar
Editar
DATABASE_URL=sqlite:///./signals.db
TELEGRAM_API_KEY=your_telegram_key_here
As chaves reais devem ser armazenadas com segurança e nunca expostas publicamente.

💡 Roadmap
 CRUD de sinais via API

 Testes automatizados com Pytest

 Integração com Telegram para captura de sinais

 Execução de ordens simuladas

 Dashboard de performance

🧑‍💻 Autor
Feito por Felipe Menegussi

