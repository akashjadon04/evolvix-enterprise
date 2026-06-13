import glob

html_files = glob.glob('*.html')

toggle_html = '''<button id="themeToggle" style="background:transparent;border:1px solid var(--border-glass);color:var(--text-primary);border-radius:50%;width:42px;height:42px;display:flex;align-items:center;justify-content:center;cursor:pointer;margin-left:0.5rem;transition:all 0.3s;font-size:1.2rem;z-index:9999;" aria-label="Toggle Theme">🌓</button>'''

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        with open(filepath, 'r', encoding='utf-16') as f:
            content = f.read()
            
    # Add Theme Toggle Button
    if 'id="themeToggle"' not in content:
        # Let's insert it inside the .nav-container, right before the closing </div> of nav-container
        # Or better, right after the closing </nav> tag
        content = content.replace('</nav>', '</nav>\n' + toggle_html)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added theme toggle to all HTML files.")
