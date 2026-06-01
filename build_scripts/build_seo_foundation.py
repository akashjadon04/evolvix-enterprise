import os
import datetime

d = 'c:/projects/evolvix'
base_url = 'https://evolnex.digital'

html_files = [f for f in os.listdir(d) if f.endswith('.html') and not f.startswith('admin')]

# Exclude specific files if needed
exclude = ['success.html']
html_files = [f for f in html_files if f not in exclude]

# Priorities
priorities = {
    'index.html': '1.0',
    'services.html': '0.9',
    'case-studies.html': '0.8',
    'about.html': '0.8',
    'pricing.html': '0.7',
    'contact.html': '0.8',
}

today = datetime.datetime.now().strftime('%Y-%m-%d')

sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for f in html_files:
    url = f"{base_url}/{f}" if f != 'index.html' else f"{base_url}/"
    priority = priorities.get(f, '0.5')
    
    sitemap_content += '  <url>\n'
    sitemap_content += f'    <loc>{url}</loc>\n'
    sitemap_content += f'    <lastmod>{today}</lastmod>\n'
    sitemap_content += f'    <changefreq>weekly</changefreq>\n'
    sitemap_content += f'    <priority>{priority}</priority>\n'
    sitemap_content += '  </url>\n'

sitemap_content += '</urlset>'

with open(os.path.join(d, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print("sitemap.xml created.")

robots_content = f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""

with open(os.path.join(d, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots_content)

print("robots.txt created.")
