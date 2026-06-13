import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'style="color:\s*#fff\s*!important;?"', 'style="color: var(--text-primary);"', c)
c = re.sub(r'style="color:\s*#fff\s*!important;\s*([^"]+)"', r'style="color: var(--text-primary); \1"', c)

# Let's also replace other hardcoded colors like `color: #fff` inside `h2` or `h3` tags if not needed.
# But just the !important ones for now.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed hardcoded whites in index.html")
