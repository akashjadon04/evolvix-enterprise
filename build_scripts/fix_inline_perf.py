import re

html_path = 'c:/projects/evolvix/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Throttle the hero-data-stream from requestAnimationFrame (60fps) to setTimeout (10fps)
html = html.replace('requestAnimationFrame(tick);', 'setTimeout(tick, 100);')
# Wait, this might replace ALL requestAnimationFrame(tick) including other functions.
# Let's do it precisely for hero-data-stream.
