import re

html_path = 'c:/projects/evolvix/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the old downloadPDF: function() { ... } block entirely
# It starts with downloadPDF: function() { and ends with }, (before the next property)
html = re.sub(r'downloadPDF:\s*function\(\)\s*\{.*?(?=\n\s*\}\s*;\s*</script>|\n\s*},\s*[a-zA-Z0-9_]+:)', '', html, flags=re.DOTALL)

# Also remove the specific block at the end of the file containing window._buildPlaybookPDF definition
# We'll just regex out the script block that defines it, or regex out the function body.
html = re.sub(r'window\._buildPlaybookPDF\s*=\s*function\(\)\s*\{.*?(?=\n\s*</script>)', '', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
