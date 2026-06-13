import os

toggle_btn = '<button class="theme-toggle-btn" style="background:transparent;border:1px solid var(--border-glass);color:var(--text-primary);border-radius:50%;width:42px;height:42px;display:flex;align-items:center;justify-content:center;cursor:pointer;margin-right:1rem;transition:all 0.3s;font-size:1.2rem;z-index:999;" aria-label="Toggle Theme">🌓</button>'

for f in ['about.html', 'contact.html', 'services.html']:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '<button class="nav-toggle"' in content and '🌓' not in content:
        content = content.replace('<button class="nav-toggle"', f'{toggle_btn}<button class="nav-toggle"')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Added themeToggle to {f}')
    else:
        print(f'Could not find nav-toggle in {f} or already added')
