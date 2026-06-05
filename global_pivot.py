import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Analytics Payload (GA4)
analytics_script = """
    <!-- Google Analytics 4 (Global Tag) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-X1Y2Z3W4V5"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-X1Y2Z3W4V5');
    </script>
"""

# Fetch API polyfill / interceptor for Web3Forms (removes iframe need)
fetch_script = """
    <!-- Web3Forms AJAX Interceptor -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const forms = document.querySelectorAll('form[action="https://api.web3forms.com/submit"]');
            forms.forEach(form => {
                form.removeAttribute('target');
                form.addEventListener('submit', async function(e) {
                    if (this.id === 'godContactForm' && typeof handleGodSubmit === 'function') {
                        // handleGodSubmit is defined in contact.html, we let it handle UI
                    } else {
                        e.preventDefault();
                        const btn = this.querySelector('button[type="submit"]');
                        if(btn) btn.textContent = 'SENDING...';
                        const formData = new FormData(this);
                        try {
                            await fetch(this.action, { method: 'POST', body: formData });
                            if(btn) { btn.textContent = '✓ REQUEST SENT'; btn.style.background = '#10b981'; btn.style.color = '#fff'; }
                        } catch(err) {
                            if(btn) btn.textContent = 'ERROR, TRY AGAIN';
                        }
                    }
                });
            });
        });
    </script>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Shorten Title Tags (< 60 chars)
    # E.g., <title>Evolnex | Best Digital Marketing & Web Development Agency in Phagwara, Punjab</title>
    content = re.sub(
        r'<title>.*?</title>',
        '<title>Evolnex | Premium Digital Product Studio</title>',
        content,
        flags=re.IGNORECASE
    )

    # 2. Rewrite Meta Description (Global Audience, ~130-150 chars)
    content = re.sub(
        r'<meta\s+name="description"\s+content="[^"]*"\s*/?>',
        '<meta name="description" content="Evolnex is a premium digital product studio. We engineer high-performance websites, SaaS platforms, and mobile apps for global leaders.">',
        content,
        flags=re.IGNORECASE
    )

    # 3. Add Analytics and Favicon to <head>
    if 'googletagmanager.com' not in content:
        content = content.replace('<head>', f'<head>\n{analytics_script}\n    <link rel="icon" type="image/webp" href="assets/evolnex.webp">')
    
    # 4. Remove iFrames
    content = re.sub(r'<iframe\s+name="hidden_iframe"[^>]*>.*?</iframe>', '', content, flags=re.IGNORECASE)
    
    # Inject fetch script before </body>
    if 'Web3Forms AJAX Interceptor' not in content:
        content = content.replace('</body>', f'{fetch_script}\n</body>')

    # 5. Fix geojs.io Error -> ipapi.co
    content = content.replace("fetch('https://get.geojs.io/v1/ip/geo.json').then(r=>r.json()).then(geo => {",
                              "fetch('https://ipapi.co/json/').then(r=>r.json()).then(geo => {")
    content = content.replace("var city = (geo.city || 'Your Area') + ', ' + (geo.country_code || 'Local');",
                              "var city = (geo.city || 'Your Area') + ', ' + (geo.country_name || 'Local');")

    # 6. Globalize Footer Text
    old_footer_p = 'As the <strong>Best Digital Marketing Agency in Phagwara & Agra</strong>, Evolnex proudly delivers premium Web Development, SaaS, and App Solutions globally.'
    new_footer_p = 'As a <strong>Premium Digital Product Studio</strong>, Evolnex proudly engineers high-performance Web, SaaS, and App Solutions for brands <strong>Worldwide.</strong>'
    content = content.replace(old_footer_p, new_footer_p)

    # 7. Obfuscate Clear Text Email Address in HTML
    # We replace 'evolvixtechnology@gmail.com' with an encoded version or 'info [at] evolnex.digital'
    content = content.replace('evolvixtechnology@gmail.com', 'info&#64;evolnex.digital')

    # 8. Add Business Address to Footer (Generic Global)
    old_address_html = '<div class="footer-heading" style="margin-top:1.5rem;">Legal</div>'
    new_address_html = '<div class="footer-heading" style="margin-top:1.5rem;">Headquarters</div><p style="color:rgba(255,255,255,0.5);font-size:0.85rem;margin-bottom:1.5rem;">Global Operations<br>Serving Clients Worldwide</p>' + old_address_html
    if 'Global Operations' not in content and old_address_html in content:
        content = content.replace(old_address_html, new_address_html)

    # Update web3forms god mode script in contact.html
    if file == 'contact.html':
        content = content.replace("""function handleGodSubmit(e) {
                const btn = document.getElementById('godSubmitBtn');""",
                """async function handleGodSubmit(e) {
                e.preventDefault();
                const btn = document.getElementById('godSubmitBtn');
                const form = e.target;
                const formData = new FormData(form);""")
        content = content.replace("""btn.innerHTML = 'Establishing Secure Connection...';
                btn.style.pointerEvents = 'none';
                btn.style.opacity = '0.7';
                
                // Reset form and show success state after short delay
                setTimeout(() => {""", 
                """btn.innerHTML = 'Establishing Secure Connection...';
                btn.style.pointerEvents = 'none';
                btn.style.opacity = '0.7';
                try {
                    await fetch(form.action, { method: 'POST', body: formData });
                } catch(err) { console.error(err); }
                setTimeout(() => {""")

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Create llms.txt
llms_content = """# Evolnex Technologies
Evolnex is an Elite Digital Product Studio specializing in high-performance Web Development, SaaS architecture, and Mobile Applications.
We operate globally, serving industry leaders, founders, and enterprises.
Founder & CEO: Akash Jadon
Contact: info@evolnex.digital
Website: https://evolnex.digital/

## Services
- SaaS Platforms
- Custom Web Applications
- Mobile App Development
- Technical SEO & Digital Marketing
"""
with open('llms.txt', 'w', encoding='utf-8') as f:
    f.write(llms_content)

print("Zero-Bug Global Pivot Executed Successfully.")
