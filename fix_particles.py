import re

with open('theme.js', 'r', encoding='utf-8') as f:
    c = f.read()

# Update toggle
if 'localStorage.setItem(\'evx-theme\', \'dark\');' in c and 'window.updateParticles(false)' not in c:
    c = c.replace(
        "localStorage.setItem('evx-theme', 'dark');",
        "localStorage.setItem('evx-theme', 'dark');\n                    if(window.updateParticles) window.updateParticles(false);"
    )

if 'localStorage.setItem(\'evx-theme\', \'light\');' in c and 'window.updateParticles(true)' not in c:
    c = c.replace(
        "localStorage.setItem('evx-theme', 'light');",
        "localStorage.setItem('evx-theme', 'light');\n                    if(window.updateParticles) window.updateParticles(true);"
    )

# Expose particles updater
if 'window.updateParticles = function' not in c:
    # Insert after `const particlesMaterial = new THREE.PointsMaterial({...});`
    # We can just insert it after `scene.add(particlesMesh);`
    insert_str = """
        window.updateParticles = function(light) {
            if(particlesMaterial) {
                particlesMaterial.color.setHex(light ? 0xf97316 : 0x67e8f9);
                particlesMaterial.blending = light ? THREE.NormalBlending : THREE.AdditiveBlending;
                particlesMaterial.needsUpdate = true;
            }
        };
"""
    c = c.replace('scene.add(particlesMesh);', 'scene.add(particlesMesh);' + insert_str)

with open('theme.js', 'w', encoding='utf-8') as f:
    f.write(c)

# Now update index.html physics-bg
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace: #physics-bg{position:absolute;top:0;left:0;width:100%;height:100%;z-index:0;opacity:.6}
# with: #physics-bg{position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;opacity:.6;pointer-events:none}
html = re.sub(
    r'#physics-bg\{position:absolute;top:0;left:0;width:100%;height:100%;z-index:0;opacity:\.6\}',
    '#physics-bg{position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;opacity:.6;pointer-events:none}',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated theme.js and index.html')
