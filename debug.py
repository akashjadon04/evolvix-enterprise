import re

c = open('index.html', encoding='utf-8').read()
matches = list(re.finditer(r'<div class="footer-socials">', c))
print('Count of <div class="footer-socials">:', len(matches))

body_match = re.search(r'<body[^>]*>', c)
print('Body tag:', body_match.group(0) if body_match else 'Not found')

canvas_match = re.search(r'<canvas[^>]*>', c)
print('Canvas tag:', canvas_match.group(0) if canvas_match else 'Not found')

# Let's check why page is stuck. Preloader maybe? Or the PageLoader overlay.
print('preloader in content:', 'id="preloader"' in c)

# Let's check the footer structure for duplication
footer_start = c.find('<footer')
print('Footer content preview:')
print(c[footer_start:footer_start+2000])

