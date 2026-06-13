with open('theme.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if '[data-theme="light"] .kinetic-word' in line or '[data-theme="light"] .word-reveal' in line:
        skip = True
        
    if not skip:
        new_lines.append(line)
        
    if skip and '}' in line:
        skip = False

with open('theme.css', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Cleaned up theme.css')
