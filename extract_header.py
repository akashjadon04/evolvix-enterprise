c = open('index.html', encoding='utf-8').read()
header = c[c.find('<header'):c.find('</header>')]
with open('header_out.txt', 'w', encoding='utf-8') as f:
    f.write(header)
