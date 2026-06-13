import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # regex to remove the style block
    pattern = re.compile(r'<style id="light-mode-forces">.*?</style>', re.DOTALL)
    new_c = pattern.sub('', c)
    
    if new_c != c:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_c)
        print(f"Removed from {file}")
