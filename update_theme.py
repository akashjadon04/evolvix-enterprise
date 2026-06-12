import re

c = open('theme.css', 'r', encoding='utf-8').read()

new_vars = '''[data-theme="light"] {
  --bg-body: #f8fafc;
  --bg-surface-1: #ffffff;
  --bg-surface-2: #f1f5f9;
  --bg-glass: rgba(255,255,255,0.7);
  --bg-glass-heavy: rgba(248,250,252,0.95);
  --text-primary: #020617;
  --text-secondary: #334155;
  --text-tertiary: #64748b;
  --text-invert: #f8fafc;
  --border-glass: rgba(0,0,0,0.08);
  --border-highlight: rgba(249,115,22,0.4);
  
  --c-brand-darkest: #431407;
  --c-brand-dark: #7c2d12;
  --c-brand-main: #f97316;
  --c-brand-glow: #fdba74;
  --c-brand-light: #fb923c;
  
  --shadow-sm: 0 2px 4px rgba(0,0,0,0.05);
  --shadow-lg: 0 20px 40px -10px rgba(0,0,0,0.1);
}'''

c = re.sub(r'\[data-theme="light"\]\s*\{[^}]*\}', new_vars, c, count=1)

extra_css = '''
[data-theme="light"] .service-card::before { background: linear-gradient(135deg, rgba(249,115,22,0.2), rgba(0,0,0,0.03) 50%, rgba(251,146,60,0.1)); }
[data-theme="light"] .kinetic-word, [data-theme="light"] .word-reveal .text-gradient .word-unit {
  background: linear-gradient(135deg, #7c2d12 10%, #f97316 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
}
[data-theme="light"] .theme-toggle-btn::after {
  background: #f97316;
  box-shadow: 0 0 10px rgba(249,115,22,0.5);
}
[data-theme="light"] .btn-primary {
  background: #f97316;
  color: #fff;
  border-color: rgba(249,115,22,0.2);
  box-shadow: 0 0 20px rgba(249,115,22,0.4);
}
[data-theme="light"] .btn-primary:hover {
  color: #fff;
  border-color: #fb923c;
  box-shadow: 0 0 40px rgba(249,115,22,0.6);
}
[data-theme="light"] .btn-primary::before {
  background: radial-gradient(circle, #fb923c 0, #f97316 100%);
}
[data-theme="light"] .float-tag { border-color: #f97316; color: #020617; }
[data-theme="light"] .process-number { color: #f97316; }
[data-theme="light"] .process-step:hover .process-number { background: #f97316; color: #fff; border-color: #fb923c; }
[data-theme="light"] .text-gradient {
  background: linear-gradient(135deg, #7c2d12 10%, #f97316 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
'''

c += extra_css
open('theme.css', 'w', encoding='utf-8').write(c)

js = open('theme.js', 'r', encoding='utf-8').read()
js = js.replace('particleMaterial.color.setHex(0x0e7490);', 'particleMaterial.color.setHex(0xf97316);')
open('theme.js', 'w', encoding='utf-8').write(js)
