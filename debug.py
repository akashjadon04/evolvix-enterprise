import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('http://localhost:8080/index.html')
        await page.wait_for_timeout(2000)
        
        # Click theme toggle to ensure light mode
        await page.click('.theme-toggle-btn')
        await page.wait_for_timeout(1000)
        
        # Log computed background of body
        bg = await page.evaluate('window.getComputedStyle(document.body).backgroundColor')
        print('body bg:', bg)
        
        # Log which element covers the viewport (100px from top)
        el = await page.evaluate('''() => {
            let e = document.elementFromPoint(100, 300);
            return e ? e.tagName + "." + e.className : "None";
        }''')
        print('element at 100,300:', el)
        
        # Get elements with dark backgrounds
        dark_els = await page.evaluate('''() => {
            let res = [];
            document.querySelectorAll('*').forEach(el => {
                let st = window.getComputedStyle(el);
                if(st.backgroundColor === 'rgb(2, 6, 23)' || st.backgroundColor === 'rgba(2, 6, 23, 1)') {
                    res.push(el.tagName + "." + el.className + " (" + el.id + ")");
                }
            });
            return res;
        }''')
        print('Dark elements:', dark_els)
        
        await browser.close()

asyncio.run(capture())
