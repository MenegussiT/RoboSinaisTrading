from playwright.async_api import async_playwright
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv('CORRETORA_LOGIN')
senha = os.getenv('CORRETORA_PASSWORD')
corretora = os.getenv('CORRETORA_URL')

async def logar_corretora():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(corretora)

        await page.wait_for_selector('input[name="username"]')
        await page.fill('input[name="username"]', email)

        await page.wait_for_selector('input[name="password"]')
        await page.fill('input[name="password"]', senha)

        await page.click('button[type="submit"]')

        print("✅ Logado com sucesso na corretora Avalon!")
        return page  # mantém a página ativa pra próximos comandos
