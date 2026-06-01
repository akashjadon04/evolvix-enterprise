import os

d = 'c:/projects/evolvix'
files = [f for f in os.listdir(d) if f.endswith('.html')]

for f in files:
    path = os.path.join(d, f)
    with open(path, 'r', encoding='utf-8') as file:
        html = file.read()
    
    html = html.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>', '<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js" defer></script>')
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(html)
