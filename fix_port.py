import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('class="portfolio-card"', 'class="portfolio-card tilt-card"')
c = c.replace('class="portfolio-link"', 'class="portfolio-link" rel="nofollow"')

c = c.replace('src="assets/ui_nexusai_1780211922385.png"', 'src="assets/nexusai_3d_1780215748199.png"')
c = c.replace('src="assets/ui_auralogistics_1780211936918.png"', 'src="assets/aura_logistics_3d_1780215765458.png"')
c = c.replace('src="assets/ui_finshift_1780211959768.png"', 'src="assets/finshift_banking_1780215791713.png"')
c = c.replace('src="assets/ui_bakestories_1780211875183.png"', 'src="assets/bakestories_pink_1780215720648.png"')

c = c.replace('height:100vh;overflow:hidden;display:flex;flex-direction:column;justify-content:center;', 'min-height:100vh;height:auto;overflow:hidden;display:flex;flex-direction:column;justify-content:center;padding:5rem 0;')

c = c.replace('background:linear-gradient(90deg,transparent,rgba(103,232,249,.3),transparent)', 'background:linear-gradient(90deg,transparent,var(--border-highlight),transparent)')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Portfolio updated successfully')
