c = open('index_old.html', 'r', encoding='utf-16').read()
start = c.find('<div class="cmd-backdrop')
with open('check_context.txt', 'w', encoding='utf-8') as f:
    f.write(c[start-100:start+100])
