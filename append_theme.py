with open('theme.css', 'a', encoding='utf-8') as f:
    f.write('''

/* FIX INVISIBLE TEXT IN DARK SECTIONS */
[data-theme="light"] .cta-card h2,
[data-theme="light"] .cta-card h3,
[data-theme="light"] .cta-card p,
[data-theme="light"] .cta-section h2,
[data-theme="light"] .cta-section h3,
[data-theme="light"] .cta-section p,
[data-theme="light"] .footer h2,
[data-theme="light"] .footer h3,
[data-theme="light"] .footer p,
[data-theme="light"] .footer a {
    color: #ffffff !important;
}

[data-theme="light"] .footer,
[data-theme="light"] .cta-section,
[data-theme="light"] .cta-card {
    background-color: #020617 !important;
}

/* FIX ALL SVGS IN LIGHT MODE */
[data-theme="light"] svg {
    filter: invert(1) brightness(0.8) !important;
}
/* Except SVGs in dark sections */
[data-theme="light"] .footer svg,
[data-theme="light"] .cta-card svg,
[data-theme="light"] .cta-section svg {
    filter: none !important;
}

/* Ensure Logo inverts properly */
[data-theme="light"] .evolnex-logo {
    filter: invert(1) !important;
}
[data-theme="light"] .footer .evolnex-logo {
    filter: none !important; /* Keep original white/blue in dark footer */
}

/* Particles should be visible */
[data-theme="light"] #webgl-hero {
    filter: none !important;
    opacity: 1 !important;
}
''')
