c = open('theme.css', encoding='utf-8').read()
idx = c.rfind('[data-theme="light"] {')
print('BEFORE:')
print(repr(c[idx-50:idx]))
