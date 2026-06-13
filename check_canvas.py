import re
c = open('index.html', encoding='utf-8').read()
match = re.search(r'<canvas id="webgl-hero".*?</canvas>', c)
if match:
    print(match.group(0))
