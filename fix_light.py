with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
    
# Inject a definitive light mode style block
light_mode_styles = '''
<style id="light-mode-forces">
html[data-theme="light"] body {
    background-color: #f8fafc !important;
    background-image: none !important;
    color: #020617 !important;
}
html[data-theme="light"] .section, 
html[data-theme="light"] .stats-section, 
html[data-theme="light"] .cta-section {
    background-color: #f8fafc !important;
}
html[data-theme="light"] .hero {
    background: radial-gradient(circle at 50% -20%, #f1f5f9 0%, #f8fafc 70%) !important;
}
html[data-theme="light"] h1, 
html[data-theme="light"] h2, 
html[data-theme="light"] h3, 
html[data-theme="light"] p, 
html[data-theme="light"] .stat-number,
html[data-theme="light"] .service-card h3,
html[data-theme="light"] .process-step h3,
html[data-theme="light"] .tech-name,
html[data-theme="light"] .portfolio-card-body h3,
html[data-theme="light"] .text-primary,
html[data-theme="light"] .kinetic-word,
html[data-theme="light"] .word-unit {
    color: #020617 !important;
    -webkit-text-fill-color: #020617 !important;
}
html[data-theme="light"] .text-gradient {
    background: linear-gradient(135deg, #f97316 10%, #ea580c 100%) !important;
    -webkit-background-clip: text !important;
    background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    color: transparent !important;
}
html[data-theme="light"] .service-card p,
html[data-theme="light"] .process-step p,
html[data-theme="light"] .portfolio-card-body p,
html[data-theme="light"] .text-secondary,
html[data-theme="light"] .text-tertiary {
    color: #334155 !important;
    -webkit-text-fill-color: #334155 !important;
}
html[data-theme="light"] .card,
html[data-theme="light"] .service-card,
html[data-theme="light"] .form-card,
html[data-theme="light"] .portfolio-card,
html[data-theme="light"] .stat-block,
html[data-theme="light"] .tech-card,
html[data-theme="light"] .cta-card {
    background: #ffffff !important;
    border-color: #cbd5e1 !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
}
html[data-theme="light"] .card::before,
html[data-theme="light"] .service-card::before,
html[data-theme="light"] .service-card::after {
    display: none !important;
}

/* Invert white/blue graphics to black/orange */
html[data-theme="light"] .hero-visual svg,
html[data-theme="light"] .footer-graphic svg,
html[data-theme="light"] svg.ambient-blob,
html[data-theme="light"] .client-logo {
    filter: invert(1) hue-rotate(180deg) brightness(0.8) !important;
}

/* Fix particle canvas */
html[data-theme="light"] #webgl-hero {
    filter: invert(1) hue-rotate(180deg) !important;
}

html[data-theme="light"] .reveal,
html[data-theme="light"] .stagger-child {
    opacity: 1 !important;
    transform: none !important;
}
html[data-theme="light"] .cmd-backdrop,
html[data-theme="light"] .cmd-palette {
    display: none !important;
}
</style>
'''
if 'id="light-mode-forces"' not in c:
    c = c.replace('</head>', light_mode_styles + '</head>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
