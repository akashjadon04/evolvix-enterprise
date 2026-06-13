import re
c = open('index.html', 'r', encoding='utf-8').read()

# 1. Rename physics-bg to webgl-hero
c = c.replace('<canvas id="physics-bg"></canvas>', '<canvas id="webgl-hero"></canvas>')
# Move webgl-hero into the body as the first element
c = re.sub(r'<canvas id="webgl-hero".*?</canvas>', '', c)
c = c.replace('<body>', '<body>\n<canvas id="webgl-hero" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1; pointer-events:none;"></canvas>')

# 2. Correctly remove the cmd-backdrop. It consists of multiple elements.
# The command palette starts with: <div class="cmd-backdrop" id="cmdBackdrop"></div>
# and ends with </div> right before <div class="cursor-dot"> or </main>
# I'll use regex to remove ONLY the command palette elements.
c = re.sub(r'<!-- ================================================================\n\s*COMMAND PALETTE.*?\n\s*================================================================ -->\s*<div class="cmd-backdrop".*?</div>\s*<div aria-label="Command palette" class="cmd-palette" id="cmdPalette" role="dialog">.*?</div>\s*</div>\s*</div>', '', c, flags=re.DOTALL)

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
    
# 4. Remove duplicate footer socials
# Wait, let's not touch this if it breaks things. Let me just replace the whole footer-socials to be exact.
# Oh, the user explicitly asked to change the social links:
# https://www.linkedin.com/company/131953983/
# https://x.com/evolnex
# https://www.instagram.com/evolnextechnologies/
# And mail to mk074377@gmail.com
# "make the mail to link, to mk074377@gmail.com that is in background"

# Remove duplicate footer-socials blocks
c = re.sub(r'<div class="footer-socials">.*?</div>\s*</div>', '', c, flags=re.DOTALL)

# 5. Fix <script src="script.js"></script> that had query params
c = re.sub(r'<script src="script\.js\?v=.*?"></script>', '<script src="script.js" defer></script>', c)
c = c.replace('<script src="script.js"></script>', '<script src="script.js" defer></script>')

# 6. Add theme.css link if not present
if 'theme.css' not in c:
    c = c.replace('</style>', '</style>\n<link rel="stylesheet" href="theme.css">')

open('index.html', 'w', encoding='utf-8').write(c)
