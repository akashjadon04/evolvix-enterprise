import os
import re

d = 'c:/projects/evolvix'
base_url = 'https://evolnex.digital'

schema_markup = """
    <!-- Local SEO JSON-LD Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ProfessionalService",
      "name": "Evolnex Technologies",
      "url": "https://evolnex.digital",
      "logo": "https://evolnex.digital/assets/evolnex.png",
      "image": "https://evolnex.digital/assets/evolnex.png",
      "description": "Best Digital Marketing & Web Development Agency in Phagwara, Agra, and Punjab. We build high-performance SaaS platforms, mobile apps, and websites.",
      "telephone": "+91-7668758238",
      "email": "evolvixtechnology@gmail.com",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Phagwara",
        "addressRegion": "Punjab",
        "addressCountry": "IN"
      },
      "areaServed": [
        "Phagwara",
        "Agra",
        "Jalandhar",
        "Ludhiana",
        "Punjab",
        "India"
      ],
      "sameAs": [
        "https://www.facebook.com/evolnex",
        "https://twitter.com/evolnex",
        "https://www.linkedin.com/company/evolnex",
        "https://www.youtube.com/@evolnex"
      ],
      "priceRange": "$$$"
    }
    </script>
"""

seo_footer_html = """
                <!-- Local SEO Footer Matrix -->
                <div class="footer-col" style="flex: 1 1 250px;">
                    <h4 class="footer-title" style="color: #fff; font-size: 1.1rem; margin-bottom: 1.5rem; font-weight: 700;">Service Areas</h4>
                    <p style="color: #94a3b8; font-size: 0.9rem; line-height: 1.6; margin-bottom: 1rem;">
                        As the <strong>Best Digital Marketing Agency in Phagwara & Agra</strong>, Evolnex Technologies proudly delivers premium Web Development, SaaS, and App Solutions to clients across <strong>Punjab, India, and Globally.</strong>
                    </p>
                    <div style="display:flex; gap: 15px; margin-top: 15px;">
                        <a href="https://linkedin.com/company/evolnex" target="_blank" rel="noopener noreferrer" style="color: #38bdf8; text-decoration: none; font-weight: bold; font-size: 0.9rem;">LinkedIn</a>
                        <a href="https://twitter.com/evolnex" target="_blank" rel="noopener noreferrer" style="color: #38bdf8; text-decoration: none; font-weight: bold; font-size: 0.9rem;">X (Twitter)</a>
                        <a href="https://facebook.com/evolnex" target="_blank" rel="noopener noreferrer" style="color: #38bdf8; text-decoration: none; font-weight: bold; font-size: 0.9rem;">Facebook</a>
                    </div>
                </div>
"""

def update_file(filepath, filename):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Fix Duplicate H1s
    h1_pattern = re.compile(r'<h1([^>]*)>(.*?)</h1>', re.IGNORECASE | re.DOTALL)
    matches = list(h1_pattern.finditer(html))
    if len(matches) > 1:
        first_match = matches[0]
        new_content = html[:first_match.end()]
        last_idx = first_match.end()
        for m in matches[1:]:
            new_content += html[last_idx:m.start()]
            attrs = m.group(1)
            inner = m.group(2)
            # Add basic styling to ensure visual consistency
            new_content += f'<div class="h1-seo"{attrs} style="display:block; font-size:inherit; font-weight:bold; margin:inherit;">{inner}</div>'
            last_idx = m.end()
        new_content += html[last_idx:]
        html = new_content

    # 2. Add Canonical and Schema
    if '<link rel="canonical"' not in html:
        canonical_url = f"{base_url}/{filename}" if filename != 'index.html' else f"{base_url}/"
        canonical_tag = f'\n    <link rel="canonical" href="{canonical_url}" />\n'
        html = html.replace('</head>', f'{canonical_tag}{schema_markup}</head>')

    # 3. Update Title
    title_map = {
        'index.html': 'Evolnex | Best Digital Marketing & Web Development Agency in Phagwara, Punjab',
        'about.html': 'About Evolnex | Top Digital Product Studio in Agra & Punjab',
        'services.html': 'Our Services | Premium Web, SaaS & App Development in India',
        'contact.html': 'Contact Evolnex | Hire the Best Digital Agency in Phagwara',
        'case-studies.html': 'Case Studies | Proven SaaS & Web Success by Evolnex',
        'pricing.html': 'Pricing | Transparent Web & App Development Rates',
    }
    
    new_title = title_map.get(filename, 'Evolnex | Elite Digital Marketing & Web Agency')
    html = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', html, flags=re.IGNORECASE)

    # 4. Update Meta Description
    desc_map = {
        'index.html': 'Looking for the best digital marketing agency in Phagwara or Agra? Evolnex builds high-performance websites, mobile apps, and SaaS platforms that scale.',
        'about.html': 'Meet the team behind Evolnex. We are the top digital product studio serving Phagwara, Punjab, and global leaders with premium software solutions.',
        'services.html': 'From cutting-edge web development to SaaS and mobile apps, Evolnex is the trusted digital agency in Punjab for brands that refuse to settle for average.',
        'contact.html': 'Ready to scale? Contact Evolnex, the premier digital marketing and web development agency in Phagwara and Agra. Let us build your next big thing.',
    }
    
    new_desc = desc_map.get(filename, 'Evolnex builds high-performance websites, mobile apps, and SaaS platforms for brands in Punjab and globally that refuse to settle for average.')
    
    if '<meta name="description"' in html:
        html = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{new_desc}">', html, flags=re.IGNORECASE)
    else:
        html = html.replace('</head>', f'\n    <meta name="description" content="{new_desc}">\n</head>')

    # 5. Inject Footer SEO Matrix
    if 'Service Areas' not in html and '<div class="footer-links">' in html:
        html = html.replace('<div class="footer-links">', f'<div class="footer-links">\n{seo_footer_html}', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

for f in os.listdir(d):
    if f.endswith('.html') and not f.startswith('admin') and f != 'success.html':
        update_file(os.path.join(d, f), f)

print("SEO optimizations applied successfully.")
