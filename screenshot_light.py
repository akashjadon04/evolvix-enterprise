from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 800})
    pg.goto('http://localhost:8080/index.html')
    pg.wait_for_timeout(2000)
    pg.evaluate("document.documentElement.setAttribute('data-theme', 'light')")
    pg.wait_for_timeout(1000)
    
    # Hide particle background just in case it breaks things
    pg.evaluate("if(document.getElementById('physics-bg')) document.getElementById('physics-bg').style.display = 'none'")
    
    pg.screenshot(path=r'C:\Users\Akash\.gemini\antigravity\brain\ba12fcf8-0dfc-4f6e-be55-1bcabe3e205f\light_mode_hero.png', full_page=False)
    
    pg.evaluate("window.scrollBy(0, 1000)")
    pg.wait_for_timeout(500)
    pg.screenshot(path=r'C:\Users\Akash\.gemini\antigravity\brain\ba12fcf8-0dfc-4f6e-be55-1bcabe3e205f\light_mode_mid.png', full_page=False)

    pg.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    pg.wait_for_timeout(500)
    pg.screenshot(path=r'C:\Users\Akash\.gemini\antigravity\brain\ba12fcf8-0dfc-4f6e-be55-1bcabe3e205f\light_mode_footer.png', full_page=False)
    
    b.close()
