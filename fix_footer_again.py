import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The exact regex to remove the 5th column (Local SEO Footer Matrix)
regex_to_remove = re.compile(r'<!-- Local SEO Footer Matrix -->\s*<div>\s*<div class="footer-heading">Service Areas</div>\s*<p style="font-size:0.8rem; color:rgba\(255,255,255,0.4\); line-height:1.6;">\s*As the <strong>Best Digital Marketing Agency in Phagwara & Agra</strong>, Evolnex Technologies proudly delivers premium Web Development, SaaS, and App Solutions to clients across <strong>Punjab, India, and Globally.</strong>\s*</p>\s*</div>', re.IGNORECASE | re.DOTALL)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the 5th column
    content = regex_to_remove.sub('', content)

    # 2. Add the SEO text safely under the logo in the 1st column, if not already there
    seo_text = '<p style="font-size:0.85rem; color:rgba(255,255,255,0.5); line-height:1.6; margin-top:1rem; margin-bottom:1.5rem;">As the <strong>Best Digital Marketing Agency in Phagwara & Agra</strong>, Evolnex proudly delivers premium Web Development, SaaS, and App Solutions globally.</p>'
    
    if seo_text not in content:
        # We find the Evolnex description paragraph in the first column and append the SEO text after it
        target_p = '<p style="font-size:0.95rem; color:rgba(255,255,255,0.55); margin-bottom:1.5rem;">Evolnex Technologies — a digital product studio that builds high-performance websites, apps, and SaaS platforms for founders who refuse to be ordinary.</p>'
        replacement = target_p + '\n                    ' + seo_text
        content = content.replace(target_p, replacement)

    # 3. Fix the footer padding so "Crafted by Akash Jadon" isn't blocked by the chatbot
    content = content.replace('padding:8rem 0 3rem;', 'padding:8rem 0 8rem;')
    content = content.replace('padding: 8rem 0 3rem;', 'padding: 8rem 0 8rem;')
    
    # 4. Remove literal newlines `\n \n`
    content = content.replace(r'\n \n', '')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Footer layout, padding, and literal newlines fixed globally.")
