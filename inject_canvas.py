from bs4 import BeautifulSoup
import os

canvas_html = '<canvas id="webgl-hero" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1; pointer-events:none;"></canvas>'

for f in os.listdir('.'):
    if f.endswith('.html') and f != 'index_old.html':
        with open(f, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            
        if not soup.find(id='webgl-hero'):
            body = soup.find('body')
            if body:
                canvas_soup = BeautifulSoup(canvas_html, 'html.parser')
                body.insert(0, canvas_soup)
                
                with open(f, 'w', encoding='utf-8') as out:
                    out.write(str(soup))
                print(f'Added webgl-hero to {f}')
