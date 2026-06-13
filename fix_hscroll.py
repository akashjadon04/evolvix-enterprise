with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix h-scroll-sticky padding
c = c.replace('.h-scroll-sticky{ position:sticky;top:0;min-height:100vh;height:auto;overflow:hidden;display:flex;flex-direction:column;justify-content:center;padding:5rem 0;}', '.h-scroll-sticky{ position:sticky;top:0;min-height:100vh;height:auto;overflow:hidden;display:flex;flex-direction:column;justify-content:center;padding:2rem 0;}')

# Add translateZ to portfolio card inner elements
css_to_add = """
.portfolio-card:hover .portfolio-card-img {
    transform: translateZ(40px) scale(1.02);
}
.portfolio-card:hover .portfolio-card-body {
    transform: translateZ(50px);
}
.portfolio-card-img, .portfolio-card-body {
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
"""

if '.portfolio-card:hover .portfolio-card-img' not in c:
    c = c.replace('.portfolio-card{ width:min(460px,82vw);', css_to_add.replace('\n', '') + '.portfolio-card{ width:min(460px,82vw);')

# Also fix the last portfolio card which still has the emoji div instead of image!
# Let me check if there's any remaining div.
if '<div style="w' in c: # I saw a truncated div earlier: <div style="w... ent:center;font-size:3.5rem;"></div>
    pass

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed h-scroll-sticky padding and added 3D depth to portfolio cards')
