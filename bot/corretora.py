from playwright.async_api import async_playwright
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

email = os.getenv('CORRETORA_LOGIN')
senha = os.getenv('CORRETORA_PASSWORD')
corretora = os.getenv('CORRETORA_URL')

browser_page = None

async def logar_corretora():
    global browser_page
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(corretora)

        await page.wait_for_selector('input[name="identifier"]')
        await page.fill('input[name="identifier"]', email)

        await page.wait_for_selector('input[name="password"]')
        await page.fill('input[name="password"]', senha)

        await page.click('button[type="submit"]')

        print("✅ Logado com sucesso na corretora Avalon!")
        return page  # mantém a página ativa pra próximos comandos
    
    browser_page = page  # Armazena a página para uso posterior

def get_browser_page():
    return browser_page  # Retorna a página armazenada

if __name__ == "__main__":
    asyncio.run(logar_corretora())