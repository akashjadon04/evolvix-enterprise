import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find the button
btn_match = re.search(r'<button aria-label="Toggle Theme" class="theme-toggle-btn".*?</button>', c, re.DOTALL)
if btn_match:
    btn_html = btn_match.group(0)
    c = c.replace(btn_html, '') # Remove it from current location

    # Find the CTA
    cta_match = re.search(r'<a class="btn btn-primary btn-cta-glow" href="/contact">\s*Start Project <span class="btn-arrow">→</span>\s*</a>', c, re.DOTALL)
    if cta_match:
        cta_html = cta_match.group(0)
        
        # Replace the CTA with the button and the CTA, grouped together
        new_cta_html = f'<div style="display:flex; align-items:center; gap:0.5rem;">\n{btn_html}\n{cta_html}\n</div>'
        c = c.replace(cta_html, new_cta_html)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(c)
        print('Moved theme toggle button')
    else:
        print('CTA not found')
else:
    print('Button not found')
