import os

target_string = "body{background-color:#020617;color:#f8fafc;font-family:'Inter',system-ui,-apple-system,sans-serif;line-height:1.6;overflow-x:hidden;position:relative}"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_string in content:
        print(f"Fixing {filepath}")
        content = content.replace(target_string, "")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f"Target string not found in {filepath}")

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in html_files:
    fix_file(file)

# also check if there's any other variations in portfolio.html and services.html
