import re
c = open('about.html', encoding='utf-8').read()
print('cmdPalette JS:', 'cmdPalette' in c)
print('cmdPalette HTML:', '<div class="cmd-palette"' in c)
print('webgl-hero:', '<canvas id="webgl-hero"' in c)
print('themeToggle:', '<button id="themeToggle"' in c)
print('theme.js:', 'theme.js' in c)
