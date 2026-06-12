import glob, re
for f in glob.glob('c:/projects/evolvix/*.html'):
    c = open(f, encoding='utf-8').read()
    # Find all start indices of <div class="footer-socials">
    starts = [m.start() for m in re.finditer(r'<div class="footer-socials">', c)]
    if len(starts) > 1:
        # For the second one onwards, find the matching </div>
        # A simple hack since we know it contains 3 <a> tags and ends with </div>
        # It's better to just use a regex
        matches = list(re.finditer(r'<div class="footer-socials">.*?</div>', c, re.DOTALL))
        if len(matches) > 1:
            for m in reversed(matches[1:]):
                c = c[:m.start()] + c[m.end():]
            open(f, 'w', encoding='utf-8').write(c)
            print('Fixed duplicate socials in', f)
