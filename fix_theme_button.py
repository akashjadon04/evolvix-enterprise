import glob

svg_sun = '''<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-sun" style="display:none;"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>'''

svg_moon = '''<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-moon"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>'''

new_button = f'''
<button aria-label="Toggle Theme" class="theme-toggle-btn" style="background:transparent;border:none;color:var(--text-primary);display:flex;align-items:center;justify-content:center;cursor:pointer;margin:0 1rem;transition:all 0.3s;padding:8px;border-radius:50%;">
{svg_sun}
{svg_moon}
</button>
'''

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    
    import re
    # Remove old button
    c = re.sub(r'<button[^>]*class="theme-toggle-btn"[^>]*>.*?</button>', '', c, flags=re.DOTALL)
    
    # Inject new button RIGHT AFTER the .nav-menu closing tag or BEFORE .nav-toggle
    # Actually, putting it next to the CTA in the nav menu is better.
    # The CTA is inside .nav-menu or .header-actions. Let's see where to put it.
    # Let's put it right before .nav-toggle so it appears on the right.
    if '<button aria-label="Open Menu"' in c:
        c = c.replace('<button aria-label="Open Menu"', new_button.strip() + '\n<button aria-label="Open Menu"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)
        print('Updated button in', file)

# Update theme.js to toggle the SVGs
js_patch = '''
// Add this to theme.js to handle SVG toggling
document.addEventListener('DOMContentLoaded', () => {
    const btns = document.querySelectorAll('.theme-toggle-btn');
    const updateIcons = () => {
        const isLight = document.documentElement.getAttribute('data-theme') === 'light';
        btns.forEach(btn => {
            const sun = btn.querySelector('.icon-sun');
            const moon = btn.querySelector('.icon-moon');
            if(sun && moon) {
                if(isLight) {
                    sun.style.display = 'block';
                    moon.style.display = 'none';
                } else {
                    sun.style.display = 'none';
                    moon.style.display = 'block';
                }
            }
        });
    };
    
    // Initial update
    updateIcons();
    
    // Bind to click
    btns.forEach(btn => {
        btn.addEventListener('click', () => {
            setTimeout(updateIcons, 10);
        });
    });
});
'''
with open('theme.js', 'a', encoding='utf-8') as f:
    f.write(js_patch)
print('Updated theme.js')
