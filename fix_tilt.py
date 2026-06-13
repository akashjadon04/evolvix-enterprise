import re
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('class="service-card holo-card reveal"', 'class="service-card holo-card reveal tilt-card"')
c = c.replace('class="process-step reveal"', 'class="process-step reveal tilt-card"')
c = c.replace('class="stat-block"', 'class="stat-block tilt-card"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Added tilt-card')
