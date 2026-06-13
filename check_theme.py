c = open('theme.css', encoding='utf-8').read()
if 'data-theme="light"' in c:
    print('light theme exists')
if '--bg-body: #ffffff !important;' in c:
    print('bg override exists')
print("End of file:")
print(c[-500:])
