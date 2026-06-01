import re
import os

d = 'c:/projects/evolvix'
files = [f for f in os.listdir(d) if f.endswith('.html')]

# We want to add preload for evolvix.webp to the head of every page.
preload_tag = '<link rel="preload" as="image" href="assets/evolvix.webp" type="image/webp">\n'

for f in files:
    path = os.path.join(d, f)
    with open(path, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # Check if preload already exists
    if 'rel="preload" as="image"' not in html and 'assets/evolvix.webp' in html:
        # Insert after <meta charset="UTF-8"> or early in the head
        if '<head>' in html:
            html = html.replace('<head>', '<head>\n    ' + preload_tag, 1)

    # Ensure script.js is deferred
    html = html.replace('<script src="script.js"></script>', '<script src="script.js" defer></script>')
    
    # Ensure all offscreen images have loading="lazy", but avoid breaking LCP images
    # We will just ensure footer images have loading="lazy" (already done mostly)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(html)

print("PageSpeed optimizations applied.")
