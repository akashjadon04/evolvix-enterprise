c = open('theme.css', encoding='utf-8').read()
idx = c.find('[data-theme="light"] {')
print('Chars before the block:')
print(c[idx-50:idx+50])
