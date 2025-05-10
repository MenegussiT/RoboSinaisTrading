from playwright.async_api import async_playwright
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

email = os.getenv('CORRETORA_LOGIN')
senha = os.getenv('CORRETORA_PASSWORD')
corretora = os.getenv('CORRETORA_URL')

playwright = None
browser = None
page = None

async def logar_corretora():
    global playwright, browser, page

    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto(corretora)

    await page.wait_for_selector('input[name="identifier"]')
    await page.fill('input[name="identifier"]', email)

    await page.wait_for_selector('input[name="password"]')
    await page.fill('input[name="password"]', senha)

    await page.click('button[type="submit"]')

    print("✅ Logado com sucesso na corretora Avalon!")
    return page

def get_browser_page():
    global page
    return page

async def executar_sinal(dados):
    page = get_browser_page()
    if page is None:
        print("❌ Página do navegador não está disponível.")
        return

    print(f"📊 Executando ordem {dados['ordem']} para o ativo {dados['ativo']}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(logar_corretora())
        loop.run_forever()  # mantém o loop aberto para possíveis comandos posteriores
    except KeyboardInterrupt:
        print("⛔ Encerrando o robô manualmente.")
    finally:
        loop.close()