import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix screen-stat-card position
c = c.replace('top:10%;right:4%;', 'top:12%;right:6%;')
c = c.replace('bottom:15%;left:4%;', 'bottom:18%;left:6%;')

# Fix float-tag positions
c = c.replace('top:-10%;right:-5%;', 'top:-18%;right:-12%;')
c = c.replace('bottom:-10%;left:-5%;', 'bottom:-18%;left:-12%;')

# Fix toggle button style
old_btn = 'style="background:transparent;border:none;color:var(--text-primary);display:flex;align-items:center;justify-content:center;cursor:pointer;margin:0 1rem;transition:all 0.3s;padding:8px;border-radius:50%;"'
new_btn = 'style="background:var(--bg-surface-2);border:1px solid var(--border-glass);color:var(--text-primary);display:flex;align-items:center;justify-content:center;cursor:pointer;margin:0 1rem;transition:all 0.3s;padding:8px;border-radius:50%;"'
c = c.replace(old_btn, new_btn)

# Make "Everything you need to" black instead of white
c = c.replace('color:#fff', 'color:var(--text-primary)')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed overlap and theme toggle')
