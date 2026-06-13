with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_html = """<nav>

<button aria-label="Open Menu" class="nav-toggle">☰</button>
<ul class="nav-menu">
<li><a class="nav-link" href="/">Home</a></li>
<li><a class="nav-link" href="/services">Services</a></li>
<li><a class="nav-link" href="/case-studies">Work</a></li>
<li><a class="nav-link" href="/pricing">Pricing</a></li>
<li><a class="nav-link" href="/about">Studio</a></li>
<li><a class="btn btn-secondary" href="/client-portal" style="padding:.5rem 1.4rem;font-size:.88rem;">Client Login</a></li>
<li class="mobile-only-item evl-disp-none"><a href="/contact" style="background:var(--c-brand-main);color:var(--text-primary);padding:1rem;border-radius:8px;font-weight:700;margin-top:1rem;display:block;text-align:center;text-decoration:none;">Start Project →</a></li>
</ul>
</nav>
<div style="display:flex; align-items:center; gap:0.5rem;">
<button aria-label="Toggle Theme" class="theme-toggle-btn" style="background:var(--bg-surface-2);border:1px solid var(--border-glass);color:var(--text-primary);display:flex;align-items:center;justify-content:center;cursor:pointer;margin:0 1rem;transition:all 0.3s;padding:8px;border-radius:50%;">
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-sun" style="display:none;"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-moon"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
</button>
<a class="btn btn-primary btn-cta-glow" href="/contact">
                Start Project <span class="btn-arrow">→</span>
</a>
</div>"""

new_html = """<div style="display:flex; align-items:center; gap:1.5rem;">
<nav>
<ul class="nav-menu">
<li><a class="nav-link" href="/">Home</a></li>
<li><a class="nav-link" href="/services">Services</a></li>
<li><a class="nav-link" href="/case-studies">Work</a></li>
<li><a class="nav-link" href="/pricing">Pricing</a></li>
<li><a class="nav-link" href="/about">Studio</a></li>
<li><a class="btn btn-secondary" href="/client-portal" style="padding:.5rem 1.4rem;font-size:.88rem;">Client Login</a></li>
<li class="mobile-only-item evl-disp-none"><a href="/contact" style="background:var(--c-brand-main);color:var(--text-primary);padding:1rem;border-radius:8px;font-weight:700;margin-top:1rem;display:block;text-align:center;text-decoration:none;">Start Project →</a></li>
</ul>
</nav>

<div style="display:flex; align-items:center; gap:0.5rem;">
<button aria-label="Toggle Theme" class="theme-toggle-btn" style="background:var(--bg-surface-2);border:1px solid var(--border-glass);color:var(--text-primary);display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all 0.3s;padding:8px;border-radius:50%;">
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-sun" style="display:none;"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-moon"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
</button>

<a class="btn btn-primary btn-cta-glow" href="/contact" style="margin: 0 0.5rem;">
                Start Project <span class="btn-arrow">→</span>
</a>
<button aria-label="Open Menu" class="nav-toggle">☰</button>
</div>
</div>"""

if old_html in c:
    c = c.replace(old_html, new_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print('Header updated')
else:
    print('Old HTML not found. Trying flexible replacement...')
    # try to just replace the nav-toggle position
    pass
