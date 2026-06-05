import os
import re

css_additions = """
/* SAFE AUDIT FIX STYLES */
.evl-disp-none { display: none; }
.evl-disp-none-center { display:none; text-align:center; padding:40px 0; }
.evl-disp-block-bold { display:block; font-size:inherit; font-weight:bold; margin:inherit; }
"""

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject the CSS into the <style> block in <head>
    if '<style>' in content and '.evl-disp-none' not in content:
        content = content.replace('<style>', '<style>\n' + css_additions + '\n')

    # 2. Fix the double class issue caused by previous script
    # This will repeatedly merge class="X" class="Y" into class="X Y" until no more are found
    old_content = None
    while old_content != content:
        old_content = content
        content = re.sub(r'class="([^"]*)"\s+class="([^"]*)"', r'class="\1 \2"', content)
        content = re.sub(r"class='([^']*)'\s+class='([^']*)'", r"class='\1 \2'", content)
        content = re.sub(r'class="([^"]*)"\s+class=\'([^"]*)\'', r'class="\1 \2"', content)
        content = re.sub(r'class=\'([^"]*)\'\s+class="([^"]*)"', r'class="\1 \2"', content)

    # 3. Remove literal \n text that appears in HTML
    content = content.replace('</div>\n\\n\n    <a href="https://wa.me', '</div>\n    <a href="https://wa.me')
    content = content.replace('</a>\n\\n\n    <!-- ENHANCED AI AUDIT', '</a>\n    <!-- ENHANCED AI AUDIT')
    
    # Just to be safe, replace any stray literal \n on its own line
    content = re.sub(r'^\s*\\n\s*$', '', content, flags=re.MULTILINE)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("True Fix Completed successfully.")
