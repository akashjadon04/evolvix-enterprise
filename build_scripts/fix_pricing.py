import re

with open('c:/projects/evolvix/pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove CSS for system-hud and live-feed
content = re.sub(r'/\*\s*FEATURE 1: SYSTEM HUD\s*\*/.*?/\*\s*FEATURE 2: QUANTUM SWITCH\s*\*/', '/* FEATURE 2: QUANTUM SWITCH */', content, flags=re.DOTALL)
content = re.sub(r'/\*\s*FEATURE 7: LIVE FEED\s*\*/.*?/\*\s*FEATURE 8: THE KILL SWITCH\s*\*/', '/* FEATURE 8: THE KILL SWITCH */', content, flags=re.DOTALL)
content = re.sub(r'\.system-hud \{ display: none; \}', '', content)
content = re.sub(r'\.live-feed \{ display: none; \}', '', content)

# Remove HTML for system-hud and live-feed
content = re.sub(r'<div class="system-hud">.*?</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="live-feed".*?</div>\s*</div>', '', content, flags=re.DOTALL)

with open('c:/projects/evolvix/pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)
