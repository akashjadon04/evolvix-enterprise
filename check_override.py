import re
c = open('theme.css', encoding='utf-8').read()
match = re.search(r'\[data-theme="light"\] \{.*?\n\}', c, flags=re.DOTALL)
if match:
    print(match.group(0))
