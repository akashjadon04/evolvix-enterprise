with open('theme.css', 'a', encoding='utf-8') as f:
    f.write('''\n
/* Invert graphics to turn white to black and blue to orange */
[data-theme="light"] .footer-graphic svg,
[data-theme="light"] .hero-visual svg,
[data-theme="light"] svg.ambient-blob,
[data-theme="light"] .client-logo {
    filter: invert(1) contrast(1.2) !important;
}

/* Hardcoded SVGs with stroke */
[data-theme="light"] svg [stroke="rgba(255,255,255,0.04)"],
[data-theme="light"] svg [stroke="rgba(103,232,249,0.06)"],
[data-theme="light"] svg [stroke="rgba(14,116,144,0.6)"],
[data-theme="light"] svg [stroke="rgba(14,116,144,0.3)"],
[data-theme="light"] svg [stroke="rgba(14,116,144,0.15)"] {
    filter: invert(1) !important;
}
''')
