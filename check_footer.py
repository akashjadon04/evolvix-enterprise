with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
    s = c.find('class="footer"')
    if s > -1:
        print(c[max(0, s):min(len(c), s+4000)].encode('ascii', 'ignore').decode('ascii'))
