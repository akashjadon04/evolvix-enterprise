import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix .hme-card background
c = c.replace('background: rgba(15,23,42,0.95);', 'background: var(--bg-glass-heavy);')

# Fix .hme-stat color
c = c.replace('color: #fff;', 'color: var(--text-primary);')

# Fix .hme-center-val color (if not already covered)
c = c.replace('.hme-center-val { font-family: var(--font-display); font-size: 3.5rem; font-weight: 900; color: #fff;', '.hme-center-val { font-family: var(--font-display); font-size: 3.5rem; font-weight: 900; color: var(--text-primary);')

# Fix .hme-center-lbl color
c = c.replace('color: rgba(255,255,255,0.9);', 'color: var(--text-secondary);')

# Fix z-index of .hme-center
c = c.replace('z-index: 2; animation: hme-float', 'z-index: 10; animation: hme-float')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed hero cards')
