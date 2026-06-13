from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:8080/index.html")
    page.wait_for_timeout(2000)
    
    # Get all matching rules for body background color
    rules = page.evaluate('''() => {
        const rules = [];
        const body = document.body;
        for (const sheet of document.styleSheets) {
            try {
                for (const rule of sheet.cssRules) {
                    if (rule.selectorText && body.matches(rule.selectorText)) {
                        if (rule.style && rule.style.backgroundColor) {
                            rules.push({
                                selector: rule.selectorText,
                                bgColor: rule.style.backgroundColor
                            });
                        }
                    }
                }
            } catch (e) {}
        }
        return rules;
    }''')
    
    print(json.dumps(rules, indent=2))
    
    browser.close()
