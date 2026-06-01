import base64
import os
import re

img_path = 'c:/projects/evolvix/assets/akash.png'
if os.path.exists(img_path):
    with open(img_path, 'rb') as f:
        img_data = f.read()
    b64 = base64.b64encode(img_data).decode('utf-8')
    data_uri = f'data:image/png;base64,{b64}'
    
    html_path = 'c:/projects/evolvix/index.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('src="assets/akash.png"', f'src="{data_uri}"')
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Converted akash.png to base64.")
else:
    print("akash.png not found!")
