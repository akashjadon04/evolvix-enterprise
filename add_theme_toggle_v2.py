import os
import re

toggle_btn = '<button id="themeToggle" style="background:transparent;border:1px solid var(--border-glass);color:var(--text-primary);border-radius:50%;width:42px;height:42px;display:flex;align-items:center;justify-content:center;cursor:pointer;margin-left:0.5rem;transition:all 0.3s;font-size:1.2rem;z-index:999;" aria-label="Toggle Theme">🌓</button>'

for f in ['about.html', 'contact.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Try inserting right after <div style="display:flex;align-items:center;gap:1.5rem;">
    # Note: in about.html it is gap:1.5rem
    pattern = re.compile(r'(<div[^>]*gap:1\.5rem;[^>]*>)', re.IGNORECASE)
    
    if pattern.search(content):
        content = pattern.sub(rf'\1\n        {toggle_btn}', content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Added themeToggle to {f}')
    else:
        print(f'Pattern not found in {f}')
