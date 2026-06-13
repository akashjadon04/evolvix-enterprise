import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Add to :root
root_end = c.find('}')
if root_end > -1 and '--c-brand-main-rgb' not in c:
    c = c[:root_end] + '--c-brand-main-rgb:14,116,144;--c-brand-light-rgb:103,232,249;' + c[root_end:]

# Replace occurrences
c = re.sub(r'rgba\(\s*14\s*,\s*116\s*,\s*144\s*,', 'rgba(var(--c-brand-main-rgb),', c)
c = re.sub(r'rgba\(\s*103\s*,\s*232\s*,\s*249\s*,', 'rgba(var(--c-brand-light-rgb),', c)

# Replace hexes outside CSS blocks?
c = c.replace('#0e7490', 'var(--c-brand-main)')
c = c.replace('#67e8f9', 'var(--c-brand-light)')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated index.html rgb values')

with open('theme.css', 'r', encoding='utf-8') as f:
    tc = f.read()

# Add to [data-theme="light"]
light_start = tc.find('[data-theme="light"] {')
if light_start > -1 and '--c-brand-main-rgb' not in tc:
    light_inner = light_start + len('[data-theme="light"] {')
    tc = tc[:light_inner] + '\n  --c-brand-main-rgb: 249, 115, 22;\n  --c-brand-light-rgb: 251, 146, 60;' + tc[light_inner:]

with open('theme.css', 'w', encoding='utf-8') as f:
    f.write(tc)

print('Updated theme.css rgb values')
