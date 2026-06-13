from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8080/index.html")
    
    # Wait for JS to load
    page.wait_for_timeout(2000)
    
    # Force light mode via JS just to be absolutely sure
    page.evaluate("document.documentElement.setAttribute('data-theme', 'light')")
    page.evaluate("localStorage.setItem('evx-theme', 'light')")
    page.evaluate("window.dispatchEvent(new Event('storage'))") # Trigger update if any
    
    # Wait for redraw
    page.wait_for_timeout(1000)
    
    # Check computed styles
    bg_body = page.evaluate("window.getComputedStyle(document.body).backgroundColor")
    text_color = page.evaluate("window.getComputedStyle(document.body).color")
    
    print("Body background-color:", bg_body)
    print("Body color:", text_color)
    
    # Check logo filter
    logo = page.locator('.evolnex-logo')
    if logo.count() > 0:
        filter_style = logo.first.evaluate("el => window.getComputedStyle(el).filter")
        print("Logo filter:", filter_style)
    else:
        print("Logo not found")
        
    # Check stats block
    stat = page.locator('.stat-block').first
    if stat.count() > 0:
        stat_bg = stat.evaluate("el => window.getComputedStyle(el).backgroundColor")
        stat_num_color = stat.locator('.stat-number').evaluate("el => window.getComputedStyle(el).color")
        print("Stat block background:", stat_bg)
        print("Stat number color:", stat_num_color)
    
    page.screenshot(path="debug_screenshot.png")
    browser.close()
