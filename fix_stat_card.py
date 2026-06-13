with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('.screen-stat-card{ position:absolute;background:rgba(2,6,23,.88);', '.screen-stat-card{ position:absolute;z-index:10;background:var(--bg-glass-heavy);')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed screen-stat-card z-index and background')
