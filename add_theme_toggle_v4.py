from bs4 import BeautifulSoup
import os

toggle_html = '<button class="theme-toggle-btn" style="background:transparent;border:1px solid var(--border-glass);color:var(--text-primary);border-radius:50%;width:42px;height:42px;display:flex;align-items:center;justify-content:center;cursor:pointer;margin-right:1rem;transition:all 0.3s;font-size:1.2rem;z-index:999;" aria-label="Toggle Theme">🌓</button>'

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            
        if soup.find(class_='theme-toggle-btn'):
            continue
            
        nav_toggle = soup.find(class_='nav-toggle')
        if nav_toggle:
            toggle_soup = BeautifulSoup(toggle_html, 'html.parser')
            nav_toggle.insert_before(toggle_soup)
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(str(soup))
            print(f'Added theme toggle to {f}')
