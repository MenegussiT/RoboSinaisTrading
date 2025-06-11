# 🤖 RoboSinaisTrading: Bot de Negociação Automatizada

---

**Eleve sua estratégia de negociação com o RoboSinaisTrading – um bot inteligente, alimentado por Python, projetado para automatizar operações de criptomoedas e forex com base em sinais em tempo real de canais do Telegram.**

Aproveitando o poder da programação assíncrona moderna e do gerenciamento robusto de dados, este projeto oferece uma solução escalável e confiável para negociação automatizada, minimizando a intervenção manual e maximizando a eficiência.

## ✨ **Principais Características e Capacidades**

* **Integração de Sinais do Telegram**: Conecta-se perfeitamente a canais específicos do Telegram para monitorar e capturar sinais de negociação em tempo real.
* **Análise Inteligente de Sinais**: Processamento avançado de linguagem natural (PNL) para extrair com precisão parâmetros críticos de negociação (ativo, hora de entrada, tipo de ordem, reentradas) de diversos formatos de mensagem.
* **Execução Automatizada de Ordens**: Executa ordens de compra/venda em uma plataforma de corretagem conectada (via automação de navegador headless com Playwright).
* **Gerenciamento Robusto de Dados**: Armazena todos os sinais recebidos, seu status e métricas de desempenho em um banco de dados PostgreSQL (com ORM SQLAlchemy) para rastreamento e análise abrangentes.
* **Rastreamento de Desempenho**: Gerencia o saldo do portfólio, rastreia ganhos e perdas e fornece insights sobre os resultados das negociações.
* **Endpoints de API Escaláveis**: Possui APIs RESTful (construídas com FastAPI) para interação programática, criação de sinais e recuperação de dados, permitindo a integração com outros sistemas ou um futuro painel.
* **Alta Confiabilidade**: Implementa testes automatizados com Pytest para garantir a qualidade e estabilidade do código em todas as funcionalidades principais.
* **Configuração Segura**: Utiliza variáveis de ambiente para chaves de API e credenciais sensíveis, promovendo práticas de implantação seguras.

## 🚀 **Tecnologias Principais Utilizadas**

* **Python 3.13**: A espinha dorsal da aplicação, garantindo alto desempenho e fácil manutenção.
* **FastAPI**: Um framework web moderno, rápido (de alto desempenho) para construir APIs robustas.
* **SQLAlchemy**: Poderoso Object Relational Mapper (ORM) para interações eficientes e flexíveis com o banco de dados.
* **PostgreSQL**: Um banco de dados relacional de código aberto confiável e escalável para armazenamento persistente de dados de negociação.
* **Telethon**: Uma biblioteca Python assíncrona para interagir com a API do Telegram.
* **Playwright**: Uma biblioteca de ponta para automação de navegador, permitindo interação confiável com plataformas de negociação.
* **Pytest**: Um framework de teste líder para escrever testes automatizados claros e concisos.
* **`python-dotenv`**: Para gerenciamento seguro de variáveis de ambiente.
* **Uvicorn**: Uma implementação de servidor web ASGI, impulsionando o FastAPI.

## ⚙️ **Estrutura do Projeto**

O repositório é organizado para clareza e modularidade, facilitando a navegação e a extensão:
```
📦 RoboSinaisTrading/
│
├── bot/                       # Lógica central do bot para integração com Telegram e execução de ordens
│   ├── corretora.py           # Interação com a corretora e login (usando Playwright)
│   ├── get_chat_ids.py        # Utilitário para buscar IDs de chat do Telegram
│   ├── main.py                # Ponto de entrada principal do bot e agendador
│   ├── message_parser.py      # Lógica para analisar sinais de Telegram recebidos
│   ├── scheduler.py           # (Planejado) Agendador de tarefas para verificações de rotina
│   └── telegram_utils.py      # Interação com a API do Telegram e manipulação de mensagens
│
├── crud/                      # Operações de Criar, Ler, Atualizar, Excluir para modelos de banco de dados
│   └── signal.py              # Operações CRUD para sinais de negociação
│
├── database/                  # Configuração e modelos do banco de dados
│   ├── db.py                  # Conexão e configuração de sessão do banco de dados PostgreSQL
│   ├── db_test.py             # Banco de dados SQLite em memória para testes
│   └── models.py              # Modelos ORM do SQLAlchemy para tabelas de banco de dados
│
├── tests/                     # Suíte de testes automatizados
│   ├── conftest.py            # Fixtures do Pytest para teste de banco de dados
│   ├── test_crud_signal.py    # Testes para operações CRUD de sinais
│   └── test_login.py          # (Planejado) Testes para login da corretora
│
├── .env.example               # Modelo para variáveis de ambiente
├── requirements.txt           # Lista de dependências Python
└── README.md                  # Visão geral e documentação do projeto
```
## 🧪 **Começando e Rodando Testes**

Para ter uma cópia local funcionando, siga estas etapas simples:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/menegussit/RoboSinaisTrading.git](https://github.com/menegussit/RoboSinaisTrading.git)
    cd RoboSinaisTrading
    ```
2.  **Crie um ambiente virtual e instale as dependências:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3.  **Configure as Variáveis de Ambiente**:
    Crie um arquivo `.env` no diretório raiz baseado em `.env.example` e preencha seus detalhes:

    ```env
    DATABASE_URL=postgresql://usuario:senha@host:porta/nome_do_banco
    TELEGRAM_API_ID=seu_telegram_api_id
    TELEGRAM_API_HASH=seu_telegram_api_hash
    TELEGRAM_SESSION_NAME=robo_sinais
    TELEGRAM_GROUP_ID_TEMP=-1002439641464 # Substitua pelo ID do seu grupo/canal alvo do Telegram
    CORRETORA_LOGIN=seu_email_da_corretora
    CORRETORA_PASSWORD=sua_senha_da_corretora
    CORRETORA_URL=url_de_login_da_corretora
    ```
    *Certifique-se de que `TELEGRAM_GROUP_ID_TEMP` esteja configurado corretamente para o ID do canal do Telegram que você deseja monitorar.*
    *As chaves de API e informações sensíveis devem ser sempre armazenadas com segurança e nunca expostas publicamente.*

4.  **Inicialize o Banco de Dados**:
    ```bash
    python database/db.py
    ```
    Isso criará as tabelas necessárias no seu banco de dados PostgreSQL configurado.

5.  **Execute o Bot**:
    ```bash
    python bot/main.py
    ```
    O bot se conectará ao Telegram e começará a ouvir mensagens no canal especificado.

6.  **Execute os Testes**:
    ```bash
    pytest tests/
    ```
    Isso executará a suíte de testes automatizados para verificar a funcionalidade do projeto.

## 💡 **Roadmap e Melhorias Futuras**

Estamos continuamente trabalhando para aprimorar o RoboSinaisTrading. Planos futuros incluem:

* **API Abrangente**: Operações CRUD (Criar, Ler, Atualizar, Excluir) completas para sinais via interface FastAPI.
* **Integração com Telegram**: Recursos avançados para captura de sinais, incluindo análise de imagens e documentos.
* **Módulo de Negociação Simulada**: Um módulo dedicado para execução de ordens simuladas, permitindo testes de estratégia sem riscos.
* **Painel Interativo**: Um painel baseado na web para monitoramento de desempenho em tempo real, gerenciamento de sinais e ajustes de estratégia.
* **Estratégias Configuráveis**: Implementar várias estratégias de negociação que podem ser selecionadas e personalizadas pelo usuário.

## 🧑‍💻 **Autor**

Feito com ❤️ por *MenegussiT*
Linkedin: https://www.linkedin.com/in/menegussi-felipe/
