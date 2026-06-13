with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

bake_div = '<div style="width:100%;height:230px;background:linear-gradient(135deg,rgba(245,158,11,.12),rgba(239,68,68,.08));border-bottom:1px solid rgba(255,255,255,.07);display:flex;align-items:center;justify-content:center;font-size:3.5rem;">🍰</div>'
bake_img = '<img alt="The Bake Stories" class="portfolio-card-img" height="230" loading="lazy" src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=600&q=70" width="600"/>'
c = c.replace(bake_div, bake_img)

code_div = '<div style="width:100%;height:230px;background:linear-gradient(135deg,rgba(239,68,68,.1),rgba(139,92,246,.08));border-bottom:1px solid rgba(255,255,255,.07);display:flex;align-items:center;justify-content:center;font-size:3.5rem;">⚙️</div>'
code_img = '<img alt="CodeMySpec AI Dev Tools" class="portfolio-card-img" height="230" loading="lazy" src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=600&q=70" width="600"/>'
c = c.replace(code_div, code_img)

seed_div = '<div style="width:100%;height:230px;background:linear-gradient(135deg,rgba(16,185,129,.1),rgba(var(--c-brand-main-rgb),.08));border-bottom:1px solid rgba(255,255,255,.07);display:flex;align-items:center;justify-content:center;font-size:3.5rem;">📊</div>'
seed_img = '<img alt="Seedtable Business Intelligence" class="portfolio-card-img" height="230" loading="lazy" src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=70" width="600"/>'
c = c.replace(seed_div, seed_img)

health_div = '<div style="width:100%;height:230px;background:linear-gradient(135deg,rgba(var(--c-brand-main-rgb),.12),rgba(var(--c-brand-light-rgb),.06));border-bottom:1px solid rgba(255,255,255,.07);display:flex;align-items:center;justify-content:center;font-size:3.5rem;">💊</div>'
health_img = '<img alt="Fountain Life HealthTech" class="portfolio-card-img" height="230" loading="lazy" src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&w=600&q=70" width="600"/>'
c = c.replace(health_div, health_img)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated portfolio images')
