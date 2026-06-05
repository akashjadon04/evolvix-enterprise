import os
import re

file_path = r"c:\projects\evolvix\index.html"
css_path = r"c:\projects\evolvix\assets\main.css"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all <style> blocks
matches = list(re.finditer(r'<style>(.*?)</style>', content, re.DOTALL))

if matches:
    print(f"Found {len(matches)} <style> blocks.")
    
    css_to_append = "\n/* --- APPENDED FROM INDEX.HTML --- */\n"
    for match in matches:
        css_to_append += match.group(1) + "\n"
        
    # Append to main.css
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(css_to_append)
        
    # Remove all <style> blocks from index.html
    new_content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print("Successfully moved all remaining inline CSS to main.css")
else:
    print("No <style> blocks found.")
