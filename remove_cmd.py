import os

def strip_cmd_palette(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_idx = content.find('<div class="cmd-backdrop" id="cmd-backdrop">')
    if start_idx != -1:
        div_count = 0
        i = start_idx
        while i < len(content):
            if content.startswith('<div', i):
                div_count += 1
                i += 4
            elif content.startswith('</div', i):
                div_count -= 1
                i += 5
                if div_count == 0:
                    end_idx = i + 1
                    while end_idx < len(content) and content[end_idx-1] != '>':
                        end_idx += 1
                    
                    new_content = content[:start_idx] + content[end_idx:]
                    print(f'Removed cmd-palette from {filepath}')
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    break
            else:
                i += 1

for f in os.listdir('.'):
    if f.endswith('.html'):
        strip_cmd_palette(f)
