import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    try:
        content = open(filepath, 'r', encoding='utf-8').read()
    except:
        content = open(filepath, 'r', encoding='utf-16').read()
    
    # 1. Fix .reveal and .stagger-child opacity
    content = content.replace('.reveal{opacity:0;', '.reveal{opacity:1;')
    content = content.replace('.stagger-child{opacity:0;', '.stagger-child{opacity:1;')
    
    # 2. Fix the mailto link
    content = re.sub(r'mailto:[^"\'?]+', 'mailto:mk074377@gmail.com', content)

    # 3. Add backlinks to footer
    footer_socials = '''<div class="footer-socials">
<a href="https://www.linkedin.com/company/131953983/" class="social-btn">Li</a>
<a href="https://x.com/evolnex" class="social-btn">X</a>
<a href="https://www.instagram.com/evolnextechnologies/" class="social-btn">Ig</a>
</div>'''
    
    # Let's see if we can safely inject the new social links. 
    # Let's replace the whole footer-socials div.
    content = re.sub(r'<div class="footer-socials">.*?</div>', footer_socials, content, flags=re.DOTALL)

    open(filepath, 'w', encoding='utf-8').write(content)

print("Updated HTML files.")

# Now let's fix theme.js colors (ensure it sets orange #f97316 for particles in light mode)
theme_js = open('theme.js', 'r', encoding='utf-8').read()
theme_js = theme_js.replace('const materialColor = isLight ? 0x0e7490 : 0x67e8f9;', 'const materialColor = isLight ? 0xf97316 : 0x67e8f9;')
theme_js = theme_js.replace('particlesMaterial.color.setHex(currentLight ? 0x0e7490 : 0x67e8f9);', 'particlesMaterial.color.setHex(currentLight ? 0xf97316 : 0x67e8f9);')
open('theme.js', 'w', encoding='utf-8').write(theme_js)

# Let's fix theme.css to make sure the light theme isn't making everything white.
theme_css = open('theme.css', 'r', encoding='utf-8').read()

# Add missing light theme color overrides for text gradients and other elements
extra_css = """
/* Make sure all hardcoded #fff text becomes dark in light mode */
[data-theme="light"] body { color: #020617; }
[data-theme="light"] .stat-number, 
[data-theme="light"] .kinetic-word,
[data-theme="light"] .word-reveal .text-gradient .word-unit,
[data-theme="light"] .text-gradient {
    background: linear-gradient(135deg, #7c2d12 10%, #f97316 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: transparent !important;
}

[data-theme="light"] h1, [data-theme="light"] h2, [data-theme="light"] h3, [data-theme="light"] h4, [data-theme="light"] h5, [data-theme="light"] h6 {
    color: #020617 !important;
}

[data-theme="light"] .card h3, [data-theme="light"] .service-card h3, [data-theme="light"] .portfolio-card-body h3, [data-theme="light"] .process-step h3 {
    color: #020617 !important;
}

[data-theme="light"] p, [data-theme="light"] .stat-label, [data-theme="light"] .service-card p, [data-theme="light"] .process-step p, [data-theme="light"] .portfolio-card-body p {
    color: #334155 !important;
}

[data-theme="light"] .btn-primary {
    background: #f97316 !important;
    color: #fff !important;
    border-color: rgba(249,115,22,0.2) !important;
    box-shadow: 0 0 20px rgba(249,115,22,0.4) !important;
}

[data-theme="light"] .btn-primary:hover {
    border-color: #fb923c !important;
    box-shadow: 0 0 40px rgba(249,115,22,0.6) !important;
}

[data-theme="light"] .float-tag { border-color: #f97316 !important; color: #020617 !important; background: #fff !important; }
[data-theme="light"] .process-number { color: #f97316 !important; background: #fff !important; }
[data-theme="light"] .process-step:hover .process-number { background: #f97316 !important; color: #fff !important; border-color: #fb923c !important; }

[data-theme="light"] .footer {
    background: #ffffff !important;
    border-top: 1px solid rgba(0,0,0,0.1) !important;
}

[data-theme="light"] .footer-heading {
    color: #334155 !important;
}

[data-theme="light"] .footer-link {
    color: #475569 !important;
}

[data-theme="light"] .footer-link:hover {
    color: #f97316 !important;
}

[data-theme="light"] .social-btn {
    background: rgba(0,0,0,0.04) !important;
    border-color: rgba(0,0,0,0.07) !important;
    color: #334155 !important;
}

[data-theme="light"] .social-btn:hover {
    background: #f97316 !important;
    color: #fff !important;
}

[data-theme="light"] .copyright {
    border-top: 1px solid rgba(0,0,0,0.1) !important;
    color: #64748b !important;
}

[data-theme="light"] .owner-signature {
    color: #64748b !important;
}

[data-theme="light"] .owner-signature:hover {
    color: #f97316 !important;
}

[data-theme="light"] .owner-signature::before {
    color: #f97316 !important;
}
"""

if '[data-theme="light"] body { color: #020617; }' not in theme_css:
    theme_css += extra_css
    open('theme.css', 'w', encoding='utf-8').write(theme_css)

print("Updated theme JS and CSS.")
