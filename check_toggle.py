import re
c = open('index.html', encoding='utf-8').read()
match = re.search(r'<button id="themeToggle".*?</button>', c)
print('themeToggle:', match is not None)

t = open('theme.js', encoding='utf-8').read()
match_js = re.search(r'const themeToggleBtn =.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n', t, flags=re.DOTALL)
if match_js:
    print('theme.js theme toggle logic:')
    print(match_js.group(0))
else:
    print("Toggle logic not found in theme.js")
