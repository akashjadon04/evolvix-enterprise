import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Title to be exactly between 50 and 60 chars
# "Evolnex | Premium Digital Product Studio & Web Agency" -> 53 chars
new_title = "<title>Evolnex | Premium Digital Product Studio & Web Agency</title>"

fb_pixel = """
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '0000000000000000');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=0000000000000000&ev=PageView&noscript=1"/></noscript>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Title Length
    content = re.sub(
        r'<title>.*?</title>',
        new_title,
        content,
        flags=re.IGNORECASE
    )

    # 2. Add Facebook Pixel right before </head>
    if 'connect.facebook.net' not in content:
        content = content.replace('</head>', f'{fb_pixel}\n</head>')

    # 3. Add Business Address and Phone with Microdata Schema to Footer
    # Looking for the Headquarters block we added earlier
    old_hq = '<div class="footer-heading" style="margin-top:1.5rem;">Headquarters</div><p style="color:rgba(255,255,255,0.5);font-size:0.85rem;margin-bottom:1.5rem;">Global Operations<br>Serving Clients Worldwide</p>'
    
    new_hq_microdata = '''<div class="footer-heading" style="margin-top:1.5rem;">Headquarters</div>
                <div itemscope itemtype="https://schema.org/LocalBusiness">
                    <meta itemprop="name" content="Evolnex Technologies">
                    <p itemprop="address" itemscope itemtype="https://schema.org/PostalAddress" style="color:rgba(255,255,255,0.5);font-size:0.85rem;margin-bottom:0.5rem;">
                        <span itemprop="streetAddress">Global Operations Center</span><br>
                        <span itemprop="addressLocality">Serving Worldwide</span>
                    </p>
                    <p style="color:rgba(255,255,255,0.5);font-size:0.85rem;margin-bottom:1.5rem;">
                        <span itemprop="telephone">+91 76687 58238</span>
                    </p>
                </div>'''
    
    content = content.replace(old_hq, new_hq_microdata)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Audit Patch Executed: Title lengthened, FB Pixel installed, LocalBusiness Microdata added to footer.")
