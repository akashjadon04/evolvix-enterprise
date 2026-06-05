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
    
    # 1. JS Syntax Fix
    if filename == 'index.html':
        broken = '</div>\n                        </div>\n                    `;\n                    \n                    \n    </script>'
        fixed = '</div>\n                        </div>\n                    `;\n                }, 500);\n            };\n        });\n    </script>'
        if broken in content:
            content = content.replace(broken, fixed)
        elif '`;\n                    \n                    \n    </script>' in content:
            content = content.replace('`;\n                    \n                    \n    </script>', '`;\n                }, 500);\n            };\n        });\n    </script>')
            
    # 2. Perfect Title Tag
    content = re.sub(
        r'<title>.*?</title>',
        '<title>Evolnex Technologies | Elite Digital Studio HQ</title>',
        content,
        flags=re.IGNORECASE
    )
    
    # 3. Clean URLs (Friendly Links)
    content = re.sub(r'href="([a-zA-Z0-9\-]+)\.html"', r'href="/\1"', content)
    content = content.replace('href="/index"', 'href="/"')

    # 4. Safely extract specific inline styles
    content = content.replace('style="display:none"', 'class="evl-disp-none"')
    content = content.replace("style='display:none'", 'class="evl-disp-none"')
    content = content.replace('style="display:none;"', 'class="evl-disp-none"')
    content = content.replace("style='display:none;'", 'class="evl-disp-none"')
    content = content.replace('style="display:none;text-align:center;padding:40px 0;"', 'class="evl-disp-none-center"')
    content = content.replace('style="display:block; font-size:inherit; font-weight:bold; margin:inherit;"', 'class="evl-disp-block-bold"')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_additions)

print("Safe Audit Fix Completed successfully.")
