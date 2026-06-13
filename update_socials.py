from bs4 import BeautifulSoup
import os

new_socials_html = '''<div class="footer-socials">
<a class="social-btn" href="https://www.linkedin.com/company/131953983/" target="_blank">in</a>
<a class="social-btn" href="https://x.com/evolnex" target="_blank">𝕏</a>
<a class="social-btn" href="https://www.instagram.com/evolnextechnologies/" target="_blank">ig</a>
</div>'''

for f in os.listdir('.'):
    if f.endswith('.html'):
        with open(f, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            
        socials = soup.find_all(class_='footer-socials')
        if not socials:
            continue
            
        modified = False
        for i, s in enumerate(socials):
            if i == 0:
                s.replace_with(BeautifulSoup(new_socials_html, 'html.parser'))
                modified = True
            else:
                s.decompose()
                modified = True
                
        if modified:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(str(soup))
            print(f'Updated socials in {f}')
