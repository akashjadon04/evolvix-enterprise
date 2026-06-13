import re
c = open('theme.css', encoding='utf-8').read()
blocks = re.finditer(r'\[data-theme="light"\] \{', c)
for m in blocks:
    idx = m.start()
    print('Block at', idx)
    print(c[idx:idx+200])
