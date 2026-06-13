import glob
import re

html_files = glob.glob('*.html')

toggle_html = '''<button id="themeToggle" style="background:transparent;border:1px solid var(--border-glass);color:var(--text-primary);border-radius:50%;width:42px;height:42px;display:flex;align-items:center;justify-content:center;cursor:pointer;margin-left:0.5rem;transition:all 0.3s;font-size:1.2rem;" aria-label="Toggle Theme">🌓</button>'''

canvas_html = '<canvas id="webgl-hero" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1; pointer-events:none;"></canvas>'

gsap_scripts = '''<!-- GSAP & Theme Script -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
<script src="theme.js" defer></script>'''

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        with open(filepath, 'r', encoding='utf-16') as f:
            content = f.read()
            
    # 1. REMOVE cmd-palette HTML
    content = re.sub(r'<div aria-label="Command palette" class="cmd-palette" id="cmdPalette" role="dialog">.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="cmd-palette" id="cmdPalette".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="cmd-backdrop" id="cmdBackdrop"></div>', '', content)
    
    # 2. REMOVE cmd-palette JS (look for keydown listener for 'k')
    content = re.sub(r'document\.addEventListener\([\'"]keydown[\'"],\s*\(?e\)?\s*=>\s*\{\s*if\s*\(\(e\.metaKey\s*\|\|\s*e\.ctrlKey\)\s*&&\s*e\.key\s*===\s*[\'"]k[\'"]\)\s*\{.*?\)\s*\}\);?', '', content, flags=re.DOTALL)
    content = re.sub(r'var palette\s*=\s*document\.getElementById\([\'"]cmdPalette[\'"]\);.*?(?=<script|</script>|<!--)', '', content, flags=re.DOTALL)

    # Clean up the inline script variables that reference cmdPalette
    content = re.sub(r'var backdrop=document.getElementById\([\'"]cmdBackdrop[\'"]\).*?;', '', content)
    
    # 3. Add Theme Toggle Button
    if 'id="themeToggle"' not in content:
        # Insert next to the Start Project button in header
        content = re.sub(r'(<a class="btn btn-primary btn-cta-glow"[^>]*>.*?</a>)', r'\1\n' + toggle_html, content, flags=re.DOTALL)

    # 4. Add WebGL Canvas just after <body>
    if '<canvas id="webgl-hero"' not in content:
        content = content.replace('<body>', '<body>\n' + canvas_html)
        content = content.replace('<body class="ch">', '<body class="ch">\n' + canvas_html)

    # 5. Add GSAP and theme.js scripts at the end if missing
    if 'theme.js' not in content:
        content = content.replace('</body>', gsap_scripts + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all HTML files.")
