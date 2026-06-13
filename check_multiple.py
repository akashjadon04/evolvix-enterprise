import re
c = open('theme.css', encoding='utf-8').read()
matches = re.finditer(r'\[data-theme="light"\] \{', c)
for m in matches:
    print('Found at', m.start())
