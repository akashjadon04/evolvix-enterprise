import re

html_path = 'c:/projects/evolvix/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the template's style to be visually hidden but actually rendered by the browser
old_style = 'style="display:none; width: 850px; background: #ffffff; font-family: \'Inter\', sans-serif;"'
new_style = 'style="position: absolute; left: -9999px; top: 0; width: 850px; background: #ffffff; font-family: \'Inter\', sans-serif;"'

html = html.replace(old_style, new_style)

# Remove the JS lines that toggle display:none
html = html.replace("element.style.display = 'block';", "")
html = html.replace("element.style.display = 'none';", "")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
