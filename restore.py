import re

c = open('index_old.html', 'r', encoding='utf-16').read()

# 1. Rename physics-bg to webgl-hero
c = c.replace('<canvas id="physics-bg"></canvas>', '<canvas id="webgl-hero"></canvas>')
# Move webgl-hero into the body as the first element
c = re.sub(r'<canvas id="webgl-hero".*?</canvas>', '', c)
c = c.replace('<body>', '<body>\n<canvas id="webgl-hero" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1; pointer-events:none;"></canvas>')

# 2. Correctly remove the cmd-backdrop. 
# It is located near the end of the file. 
c = re.sub(r'<div class="cmd-backdrop[^>]*>.*?</div>\s*<div class="cmd-palette[^>]*>.*?</div>\s*</div>', '', c, flags=re.DOTALL)
# Also remove any leftover cmd-backdrop or cmd-palette if regex failed
start = c.find('<div class="cmd-backdrop')
if start != -1:
    end = c.find('<footer', start)
    if end != -1:
        c = c[:start] + c[end:]

# 3. Add GSAP scripts if not present
GSAP_SCRIPTS = '''
<!-- GSAP & Theme Script -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
<script src="theme.js" defer></script>
'''
if 'theme.js' not in c:
    c = c.replace('</body>', GSAP_SCRIPTS + '\n</body>')
    
# 4. Remove duplicate footer socials (fix from my previous script)
# Find the footer-socials block
social_block_regex = r'<div class="footer-socials">\s*<a href="https://www.linkedin.com/company/131953983/".*?</div>'
# findall to see how many exist
matches = re.findall(social_block_regex, c, re.DOTALL)
if len(matches) > 1:
    # keep only one by replacing the first occurrence with a temporary token
    c = re.sub(social_block_regex, '___SOCIAL_BLOCK___', c, count=1, flags=re.DOTALL)
    # remove the rest
    c = re.sub(social_block_regex, '', c, flags=re.DOTALL)
    # put the first one back
    c = c.replace('___SOCIAL_BLOCK___', matches[0])

# 5. Fix <script src="script.js"></script> that had query params
c = re.sub(r'<script src="script\.js\?v=.*?"></script>', '<script src="script.js" defer></script>', c)
c = c.replace('<script src="script.js"></script>', '<script src="script.js" defer></script>')

# 6. Add theme.css link if not present
if 'theme.css' not in c:
    c = c.replace('</style>', '</style>\n<link rel="stylesheet" href="theme.css">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
