from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8080/index.html")
    page.wait_for_timeout(2000)
    
    cssText = page.evaluate('''() => {
        const body = document.body;
        for (const sheet of document.styleSheets) {
            try {
                for (const rule of sheet.cssRules) {
                    if (rule.selectorText === "body" && rule.style && rule.style.backgroundColor === "rgb(2, 6, 23)") {
                        return sheet.ownerNode.outerHTML;
                    }
                }
            } catch (e) {}
        }
        return "Not found";
    }''')
    
    print(cssText)
    
    browser.close()
