import os

file_path = r"c:\projects\evolvix\index.html"
css_path = r"c:\projects\evolvix\assets\main.css"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if "<style>" in line and start_idx == -1:
        start_idx = i
    if "</style>" in line and start_idx != -1 and end_idx == -1:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    css_content = []
    # Extract from start_idx + 1 to end_idx
    # Wait, end_idx might have </style> on the same line.
    
    # Actually, we want to extract the exact text between <style> and </style>
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    import re
    # Find the FIRST <style>...</style> block
    match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if match:
        css_text = match.group(1)
        
        # Write to assets/main.css
        with open(css_path, "w", encoding="utf-8") as f:
            f.write(css_text)
            
        # Replace the first style block with a link tag
        new_content = content[:match.start()] + '<link rel="stylesheet" href="assets/main.css">' + content[match.end():]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Successfully extracted CSS to assets/main.css")
    else:
        print("No style block found")
else:
    print("Could not find style tags")
