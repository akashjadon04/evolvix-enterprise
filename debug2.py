import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('http://localhost:8080/index.html')
        await page.wait_for_timeout(1000)
        
        await page.click('.theme-toggle-btn')
        await page.wait_for_timeout(1000)
        
        bg_body = await page.evaluate('window.getComputedStyle(document.documentElement).getPropertyValue("--bg-body")')
        print('html --bg-body:', bg_body)
        
        bg_body2 = await page.evaluate('window.getComputedStyle(document.body).getPropertyValue("--bg-body")')
        print('body --bg-body:', bg_body2)

        bg = await page.evaluate('window.getComputedStyle(document.body).backgroundColor')
        print('body bg:', bg)
        
        await browser.close()

asyncio.run(capture())
