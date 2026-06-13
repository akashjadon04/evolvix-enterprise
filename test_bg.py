from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto('http://localhost:8080/index.html')
    pg.wait_for_timeout(1000)
    pg.evaluate("document.documentElement.setAttribute('data-theme', 'light')")
    pg.wait_for_timeout(500)
    print('body bg:', pg.evaluate("window.getComputedStyle(document.body).backgroundColor"))
    print('body color:', pg.evaluate("window.getComputedStyle(document.body).color"))
    b.close()
