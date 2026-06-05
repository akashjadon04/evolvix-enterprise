import os
import re

html_path = r"c:\projects\evolvix\index.html"
css_path = r"c:\projects\evolvix\assets\main.css"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Inline CSS
if '<link rel="stylesheet" href="assets/main.css">' in html:
    html = html.replace('<link rel="stylesheet" href="assets/main.css">', '<style>\n' + css + '\n</style>')
    print("Inlined CSS")

# 2. Defer Google Analytics
ga_original = """    <!-- Google Analytics 4 (Global Tag) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-X1Y2Z3W4V5"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-X1Y2Z3W4V5');
    </script>"""

ga_deferred = """    <!-- Google Analytics 4 (Global Tag) - Deferred -->
    <script>
      window.addEventListener('load', function() {
        setTimeout(function() {
          var s = document.createElement('script');
          s.src = "https://www.googletagmanager.com/gtag/js?id=G-X1Y2Z3W4V5";
          s.async = true;
          document.head.appendChild(s);
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          window.gtag = gtag;
          gtag('js', new Date());
          gtag('config', 'G-X1Y2Z3W4V5');
        }, 3500);
      });
    </script>"""

if ga_original in html:
    html = html.replace(ga_original, ga_deferred)
    print("Deferred GA")

# 3. Defer Facebook Pixel
fb_original = """<!-- Meta Pixel Code -->
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
<noscript><img height="1" width="1" class="evl-disp-none" src="https://www.facebook.com/tr?id=0000000000000000&ev=PageView&noscript=1"/></noscript>"""

fb_deferred = """<!-- Meta Pixel Code - Deferred -->
<script>
window.addEventListener('load', function() {
  setTimeout(function() {
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
  }, 4000);
});
</script>
<noscript><img height="1" width="1" class="evl-disp-none" src="https://www.facebook.com/tr?id=0000000000000000&ev=PageView&noscript=1"/></noscript>"""

if fb_original in html:
    html = html.replace(fb_original, fb_deferred)
    print("Deferred FB Pixel")

# 4. Fix http redirects
if 'http://evolnex.digital' in html:
    html = html.replace('http://evolnex.digital', 'https://evolnex.digital')
    print("Fixed HTTP redirects")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("All performance optimizations applied successfully.")
