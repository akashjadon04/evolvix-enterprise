import os

d = 'c:/projects/evolvix'

seo_footer_html = """
            <!-- Local SEO Footer Matrix -->
            <div>
                <div class="footer-heading">Service Areas</div>
                <p style="color: rgba(255,255,255,.5); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1rem;">
                    As the <strong>Best Digital Marketing Agency in Phagwara & Agra</strong>, Evolnex Technologies proudly delivers premium Web Development, SaaS, and App Solutions to clients across <strong>Punjab, India, and Globally.</strong>
                </p>
                <div style="display:flex; flex-direction:column; gap: 8px;">
                    <a href="https://linkedin.com/company/evolnex" target="_blank" rel="noopener noreferrer" class="footer-link">LinkedIn</a>
                    <a href="https://twitter.com/evolnex" target="_blank" rel="noopener noreferrer" class="footer-link">X (Twitter)</a>
                    <a href="https://facebook.com/evolnex" target="_blank" rel="noopener noreferrer" class="footer-link">Facebook</a>
                    <a href="https://youtube.com/@evolnex" target="_blank" rel="noopener noreferrer" class="footer-link">YouTube</a>
                </div>
            </div>
"""

for f in os.listdir(d):
    if f.endswith('.html') and not f.startswith('admin') and f != 'success.html':
        filepath = os.path.join(d, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            html = file.read()
        
        if 'Service Areas' not in html and '<div class="container footer-grid">' in html:
            html = html.replace('<div class="container footer-grid">', f'<div class="container footer-grid">\n{seo_footer_html}', 1)
            
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(html)

print("Footer SEO Matrix injected.")
