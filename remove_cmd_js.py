import os
import re

def strip_cmd_palette(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig_content = content
    
    # Remove the JS block in index.html, about.html, etc.
    pattern_js = re.compile(r'/\* --- 1\. Command Palette Logic --- \*/.*?/\* --- 2\. Scroll-Spy Minimap --- \*/', re.DOTALL)
    if pattern_js.search(content):
        content = pattern_js.sub('/* --- 2. Scroll-Spy Minimap --- */', content)
        print(f'Removed cmd palette JS from {filepath}')
    
    # Remove the cmd backdrop html if exists
    content = re.sub(r'<!-- Command Palette HTML -->.*?<div class="cmd-palette-backdrop" id="cmdBackdrop">.*?(?=<!-- Minimap HTML -->)', '', content, flags=re.DOTALL)
    
    # Also in services.html minified block
    content = re.sub(r'document\.addEventListener\(\'keydown\',function\(e\)\{var isMac.*?closeCmd\(\);\}\}\);\n', '', content, flags=re.DOTALL)
    
    # Also remove "cmd-backdrop" elements if they exist
    content = re.sub(r'<div class="cmd-backdrop".*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    
    if content != orig_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Saved changes to {filepath}')

for f in os.listdir('.'):
    if f.endswith('.html'):
        strip_cmd_palette(f)
