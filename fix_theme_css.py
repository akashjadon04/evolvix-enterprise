import os

theme_css = open('theme.css', 'r', encoding='utf-8').read()

# Make sure we have the variable overrides
vars_css = """
[data-theme="light"] {
    --c-brand-darkest: #f8fafc !important;
    --c-brand-dark: #f1f5f9 !important;
    --c-brand-main: #f97316 !important;
    --c-brand-glow: #fb923c !important;
    --c-brand-light: #fdba74 !important;
    
    --bg-body: #ffffff !important;
    --bg-surface-1: #f8fafc !important;
    --bg-surface-2: #f1f5f9 !important;
    --bg-glass: rgba(255,255,255,0.85) !important;
    --bg-glass-heavy: rgba(255,255,255,0.95) !important;
    
    --border-glass: rgba(0,0,0,0.1) !important;
    --border-highlight: rgba(249,115,22,0.4) !important;
    
    --text-primary: #020617 !important;
    --text-secondary: #334155 !important;
    --text-tertiary: #475569 !important;
    --text-invert: #ffffff !important;
}

[data-theme="light"] .evolnex-logo,
[data-theme="light"] .footer-evolnex-logo {
    filter: brightness(0) !important; /* Turns white logo to black */
}

/* Fix any remaining hardcoded whites */
[data-theme="light"] .service-card h3,
[data-theme="light"] .process-step h3,
[data-theme="light"] .portfolio-card-body h3,
[data-theme="light"] .card-icon,
[data-theme="light"] .tech-name,
[data-theme="light"] .astra-header-info h4,
[data-theme="light"] .astra-msg.bot {
    color: #020617 !important;
}

[data-theme="light"] .service-card p,
[data-theme="light"] .process-step p,
[data-theme="light"] .portfolio-card-body p,
[data-theme="light"] .tech-category-label {
    color: #334155 !important;
}

[data-theme="light"] .service-num {
    color: rgba(0,0,0,0.08) !important;
}

[data-theme="light"] .hero-badge {
    color: #020617 !important;
    background: rgba(255,255,255,0.9) !important;
    border-color: rgba(0,0,0,0.1) !important;
}

[data-theme="light"] .card-icon {
    background: linear-gradient(135deg, rgba(249,115,22,0.2), rgba(0,0,0,0.05)) !important;
}

[data-theme="light"] .service-card {
    background: linear-gradient(145deg, #f8fafc, #f1f5f9) !important;
    border: 1px solid rgba(0,0,0,0.05) !important;
}

[data-theme="light"] .tech-card {
    background: #f8fafc !important;
    border-color: rgba(0,0,0,0.05) !important;
}

[data-theme="light"] .tech-card:hover {
    background: #ffffff !important;
    box-shadow: 0 16px 36px rgba(249,115,22,0.15) !important;
}

[data-theme="light"] .btn-primary {
    background: #f97316 !important;
    color: #fff !important;
    box-shadow: 0 0 20px rgba(249,115,22,0.4) !important;
}
[data-theme="light"] .btn-primary:hover {
    box-shadow: 0 0 40px rgba(249,115,22,0.6) !important;
}

[data-theme="light"] .astra-chat-window {
    background: rgba(255,255,255,0.95) !important;
    border-color: rgba(0,0,0,0.1) !important;
}
[data-theme="light"] .astra-chat-header {
    background: #f8fafc !important;
    border-color: rgba(0,0,0,0.1) !important;
}
[data-theme="light"] .astra-msg.user {
    background: #f97316 !important;
    color: #fff !important;
}
"""

if '--c-brand-darkest: #f8fafc' not in theme_css:
    theme_css += "\n" + vars_css
    open('theme.css', 'w', encoding='utf-8').write(theme_css)

print("Added variables to theme.css")
