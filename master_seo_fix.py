import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# 1. Footer Removal Regex
footer_regex = re.compile(r'<!-- Local SEO Footer Matrix -->[\s\S]*?</div>\s*</div>', re.IGNORECASE)

# 2. Canonical Regex
canonical_regex = re.compile(r'<link\s+rel=["\']canonical["\']\s+href=["\']https?://(?:www\.)?evolnex\.in.*?["\']\s*/?>', re.IGNORECASE)

# 3. OG URL Regex
og_url_regex = re.compile(r'<meta\s+property=["\']og:url["\']\s+content=["\']https?://(?:www\.)?evolnex\.in.*?["\']\s*/?>', re.IGNORECASE)

# 4. JSON-LD Schema Payload
god_tier_json = """    <!-- God-Tier SEO Knowledge Graph & Semantic Authority Schema -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "WebSite",
          "@id": "https://evolnex.digital/#website",
          "url": "https://evolnex.digital/",
          "name": "Evolnex Technologies",
          "description": "Premium Digital Marketing & Web Development Agency in Phagwara and Agra. We build SaaS, Apps, and Digital Empires.",
          "publisher": {
            "@id": "https://evolnex.digital/#organization"
          }
        },
        {
          "@type": "Organization",
          "@id": "https://evolnex.digital/#organization",
          "name": "Evolnex Technologies",
          "url": "https://evolnex.digital/",
          "logo": {
            "@type": "ImageObject",
            "url": "https://evolnex.digital/assets/evolnex.webp",
            "width": 160,
            "height": 69
          },
          "founder": {
            "@id": "https://evolnex.digital/#founder"
          },
          "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+91-7668758238",
            "contactType": "customer service",
            "areaServed": ["IN", "US", "GB", "CA", "AE"],
            "availableLanguage": ["English", "Hindi"]
          },
          "sameAs": [
            "https://linkedin.com/company/evolnex",
            "https://twitter.com/evolnex",
            "https://facebook.com/evolnex",
            "https://youtube.com/@evolnex"
          ]
        },
        {
          "@type": "LocalBusiness",
          "@id": "https://evolnex.digital/#localbusiness",
          "name": "Evolnex Digital Marketing & Web Development",
          "image": "https://evolnex.digital/assets/evolnex.webp",
          "telephone": "+91-7668758238",
          "email": "evolvixtechnology@gmail.com",
          "priceRange": "$$$",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "GNA University Campus",
            "addressLocality": "Phagwara",
            "addressRegion": "Punjab",
            "postalCode": "144401",
            "addressCountry": "IN"
          },
          "geo": {
            "@type": "GeoCoordinates",
            "latitude": 31.2559,
            "longitude": 75.7933
          },
          "parentOrganization": {
            "@id": "https://evolnex.digital/#organization"
          }
        },
        {
          "@type": "Person",
          "@id": "https://evolnex.digital/#founder",
          "name": "Akash Jadon",
          "jobTitle": ["Founder & CEO", "Top SEO Specialist", "Digital Marketing Expert", "Full-Stack Developer"],
          "description": "Akash Jadon is the Founder and CEO of Evolnex Technologies. He is recognized as a Top SEO Specialist and Elite Software Architect in Agra and Punjab, specializing in exponential growth marketing, Lead Generation, and high-performance SaaS scaling.",
          "url": "https://evolnex.digital/about.html",
          "sameAs": [
            "https://linkedin.com/in/akashjadon04",
            "https://twitter.com/akashjadon04",
            "https://github.com/akashjadon04"
          ],
          "knowsAbout": [
            "Search Engine Optimization (SEO)",
            "Local SEO",
            "Technical SEO",
            "SaaS Architecture",
            "Digital Marketing",
            "Conversion Rate Optimization (CRO)"
          ],
          "alumniOf": {
            "@type": "CollegeOrUniversity",
            "name": "GNA University"
          },
          "worksFor": {
            "@id": "https://evolnex.digital/#organization"
          }
        }
      ]
    }
    </script>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # --- FOOTER FIX ---
    # 1. Remove the 5-column chunk entirely
    content = footer_regex.sub('', content)

    # 2. Re-inject the SEO text into the first column (under the logo) safely
    target_p = 'Evolnex Technologies — a digital product studio that builds high-performance websites, apps, and SaaS platforms for founders who refuse to be ordinary.'
    seo_p = 'As the <strong>Best Digital Marketing Agency in Phagwara & Agra</strong>, Evolnex proudly delivers premium Web Development, SaaS, and App Solutions globally.'
    
    if seo_p not in content and target_p in content:
        content = content.replace(target_p, target_p + '</p>\n                <p style="font-size:.85rem;margin-bottom:1.5rem;color:rgba(255,255,255,.45);line-height:1.6;">' + seo_p)

    # 3. Fix the footer padding so "Crafted by Akash Jadon" isn't blocked by the chatbot
    content = content.replace('padding:8rem 0 3rem;', 'padding:8rem 0 8rem;')
    content = content.replace('padding: 8rem 0 3rem;', 'padding: 8rem 0 8rem;')
    
    # 4. Remove literal "\n \n" text
    content = content.replace(r'\n \n', '')

    # --- SEO HACKS ---
    # 5. Fix Canonicals
    filename = os.path.basename(file)
    canonical_url = f"https://evolnex.digital/{filename}" if filename != "index.html" else "https://evolnex.digital/"
    
    if canonical_regex.search(content):
        content = canonical_regex.sub(f'<link rel="canonical" href="{canonical_url}">', content)
    else:
        # If it doesn't exist, we add it right after <head>
        content = content.replace('<head>', f'<head>\n    <link rel="canonical" href="{canonical_url}">')

    # 6. Fix OpenGraph URLs
    if og_url_regex.search(content):
        content = og_url_regex.sub(f'<meta property="og:url" content="{canonical_url}">', content)
    else:
        content = content.replace('<head>', f'<head>\n    <meta property="og:url" content="{canonical_url}">\n    <meta property="og:type" content="business.business">\n    <meta name="twitter:card" content="summary_large_image">')

    # 7. Inject God-Tier JSON-LD
    # First, let's strip out the old basic JSON-LD
    old_json_regex = re.compile(r'<script type="application/ld\+json">[\s\S]*?</script>', re.IGNORECASE)
    content = old_json_regex.sub('', content)

    # Inject the new one before </head>
    content = content.replace('</head>', god_tier_json + '</head>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Master Script Executed: Footer Fixed, Canonicals Rewritten, God-Tier JSON-LD Injected.")
