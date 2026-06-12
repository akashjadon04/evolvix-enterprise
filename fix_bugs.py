import glob

# HTML files
files = glob.glob('c:/projects/evolvix/*.html')

for fname in files:
    try:
        with open(fname, encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # Fix 1: Move canvas into body for index.html
        if fname.endswith('index.html'):
            canvas_str = '<canvas id="webgl-hero" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1; pointer-events:none;"></canvas>'
            if canvas_str in content and canvas_str + '\n<body>' in content:
                # Remove it from before body
                content = content.replace(canvas_str + '\n<body>', '<body>\n' + canvas_str)

        # Fix 2: Remove duplicate footer-socials
        # First, find if there are multiple
        socials_start = '<div class="footer-socials">'
        count = content.count(socials_start)
        if count > 1:
            # We want to remove the last occurrence, or just one of them.
            # The structure is: <div class="footer-socials"> ... </div>
            # Let's find the first one, skip it, and then remove the second one.
            first_idx = content.find(socials_start)
            second_idx = content.find(socials_start, first_idx + 1)
            
            if second_idx != -1:
                # Find the closing </div> for the second one
                # A simple way since we know the exact HTML injected:
                exact_block = '''<div class="footer-socials">
<a class="social-btn" href="https://www.linkedin.com/company/131953983/" target="_blank" rel="noopener noreferrer" aria-label="Evolnex on LinkedIn" title="LinkedIn">
<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
</a>
<a class="social-btn" href="https://x.com/evolnex" target="_blank" rel="noopener noreferrer" aria-label="Evolnex on X" title="X">
<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.737-8.835L1.254 2.25H8.08l4.253 5.622zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
</a>
<a class="social-btn" href="https://www.instagram.com/evolnextechnologies/" target="_blank" rel="noopener noreferrer" aria-label="Evolnex on Instagram" title="Instagram">
<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
</a>
</div>'''
                if content.count(exact_block) > 1:
                    # replace the last occurrence
                    content = content[::-1].replace(exact_block[::-1], '', 1)[::-1]
                else:
                    print(f"Could not find exact block to remove in {fname}")

        if original != content:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Fixed {fname}")
            
    except Exception as e:
        print(f"[ERROR] {fname}: {e}")
