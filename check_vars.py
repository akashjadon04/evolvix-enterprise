from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8080/index.html")
    page.wait_for_timeout(2000)
    
    # Check default
    bg_body_var = page.evaluate("window.getComputedStyle(document.documentElement).getPropertyValue('--bg-body')")
    print("Default --bg-body:", bg_body_var)
    
    # Force light mode
    page.evaluate("document.documentElement.setAttribute('data-theme', 'light')")
    page.wait_for_timeout(1000)
    
    bg_body_var_light = page.evaluate("window.getComputedStyle(document.documentElement).getPropertyValue('--bg-body')")
    print("Light --bg-body:", bg_body_var_light)
    
    bg_color = page.evaluate("window.getComputedStyle(document.body).backgroundColor")
    print("Body bg color:", bg_color)
    
    # Are there any other rules on body?
    bg_img = page.evaluate("window.getComputedStyle(document.body).backgroundImage")
    print("Body bg image:", bg_img[:50] + "...")
    
    browser.close()
