from bs4 import BeautifulSoup
import os

with open('index.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
    
grid = soup.find(class_='footer-grid')
if grid:
    first_col = grid.find('div')
    if first_col and not first_col.find(class_='footer-socials'):
        socials_html = '''<div class="footer-socials">
<a class="social-btn" href="https://www.linkedin.com/company/131953983/" target="_blank">in</a>
<a class="social-btn" href="https://x.com/evolnex" target="_blank">𝕏</a>
<a class="social-btn" href="https://www.instagram.com/evolnextechnologies/" target="_blank">ig</a>
</div>'''
        socials_soup = BeautifulSoup(socials_html, 'html.parser')
        
        # We find all paragraphs in the first column and append after the last one
        paragraphs = first_col.find_all('p')
        if paragraphs:
            paragraphs[-1].insert_after(socials_soup)
        else:
            first_col.append(socials_soup)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print('Injected socials into index.html')
