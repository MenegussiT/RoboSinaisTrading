# bot/corretora.py

from playwright.async_api import async_playwright
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

email = os.getenv('CORRETORA_LOGIN')
senha = os.getenv('CORRETORA_PASSWORD')
corretora = os.getenv('CORRETORA_URL')

playwright_instance = None
browser = None
page = None

async def logar_corretora():
    global playwright_instance, browser, page

    if page and not page.is_closed(): # Verifica se já está logado e a página não foi fechada
        print("✅ Já logado na corretora.")
        return page

    playwright_instance = await async_playwright().start()
    browser = await playwright_instance.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto(corretora)

    await page.wait_for_selector('input[name="identifier"]')
    await page.fill('input[name="identifier"]', email)

    await page.wait_for_selector('input[name="password"]')
    await page.fill('input[name="password"]', senha)

    await page.click('button[type="submit"]')

    # Adicione waits adicionais aqui se a página demorar para carregar ou redirecionar
    # Ex: await page.wait_for_url('https://sua-corretora.com/dashboard')
    # Ex: await page.wait_for_selector('seletor-de-elemento-na-dashboard')

    print("✅ Logado com sucesso na corretora Avalon!")
    return page

def get_browser_page():
    global page
    return page

async def executar_sinal(dados):
    page = get_browser_page()
    if page is None or page.is_closed():
        print("❌ Página do navegador não está disponível ou foi fechada. Tentando relogar...")
        await logar_corretora() # Tenta relogar se a página não estiver disponível
        page = get_browser_page()
        if page is None or page.is_closed():
            print("❌ Falha ao obter página do navegador após tentativa de relogin.")
            return

    ativo = dados['ativo']
    ordem = dados['ordem'].lower() # 'compra' ou 'venda'

    print(f"📊 Executando ordem {ordem.upper()} para o ativo {ativo}")

    try:
        # --- Lógica para interagir com a corretora ---
        # ESTE É UM EXEMPLO GENÉRICO. VOCÊ PRECISA ADAPTAR AO HTML DA SUA CORRETORA.
        # 1. Selecionar o Ativo (Exemplo: Pode ser um dropdown, input, ou link)
        # await page.fill('input[placeholder="Buscar ativo"]', ativo)
        # await page.press('input[placeholder="Buscar ativo"]', 'Enter')

        # 2. Selecionar o Botão de Compra/Venda
        # VOCÊ PRECISA INSPECIONAR OS ELEMENTOS REAIS DOS BOTÕES DE COMPRA/VENDA.
        if ordem == 'compra':
            await page.click('button[data-action="buy"]', timeout=5000) # Exemplo de seletor
            print("Clicou em COMPRA.")
        elif ordem == 'venda':
            await page.click('button[data-action="sell"]', timeout=5000) # Exemplo de seletor
            print("Clicou em VENDA.")
        else:
            print(f"❌ Ordem '{ordem}' não reconhecida.")
            return

        # 3. Confirmar a Operação (se houver um popup ou etapa de confirmação)
        # await page.wait_for_selector('button[id="confirm-order"]', timeout=5000)
        # await page.click('button[id="confirm-order"]')
        # print("Ordem confirmada.")

        print(f"✅ Ordem {ordem.upper()} para {ativo} executada com sucesso (simulado).")

    except Exception as e:
        print(f"❌ Erro ao executar sinal para {ativo} ({ordem}): {e}")


if __name__ == "__main__":
    async def run_corretora_test():
        await logar_corretora()
        # Exemplo de teste para executar sinal:
        # test_dados = {'ativo': 'EURUSD', 'ordem': 'compra'}
        # await executar_sinal(test_dados)
        await asyncio.sleep(60) # Mantém a página aberta por 60 segundos para inspeção
        if browser:
            await browser.close()
        if playwright_instance:
            await playwright_instance.stop()

    asyncio.run(run_corretora_test())