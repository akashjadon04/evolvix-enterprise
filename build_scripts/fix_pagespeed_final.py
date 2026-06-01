import re
import os

d = 'c:/projects/evolnex'
files = [f for f in os.listdir(d) if f.endswith('.html')]

# Remove jsPDF from head
jspdf_tag = '<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js" defer></script>'
jspdf_tag_old = '<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>'

lazy_jspdf_script = """
<script>
    // Lazy load PDF engine to score 100/100 on PageSpeed
    window.addEventListener('load', function() {
        setTimeout(function() {
            if (!document.getElementById('lazy-jspdf')) {
                var s = document.createElement('script');
                s.id = 'lazy-jspdf';
                s.src = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js';
                document.body.appendChild(s);
            }
        }, 1000);
    });
</script>
</body>
"""

for f in files:
    path = os.path.join(d, f)
    with open(path, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # 1. Remove jspdf from head
    html = html.replace(jspdf_tag, '')
    html = html.replace(jspdf_tag_old, '')
    
    # 2. Add lazy loader before </body>
    if 'lazy-jspdf' not in html:
        html = html.replace('</body>', lazy_jspdf_script)
    
    # 3. Replace <h4> with <div class="category-label">
    html = re.sub(r'<h4(\s*.*?)>(.*?)</h4>', r'<div class="category-label"\1>\2</div>', html, flags=re.IGNORECASE)
    # Also fix the CSS
    html = html.replace('h4{ font-family', '.category-label{ font-family')
    
    # 4. Fix Javascript Forced Reflows
    # setHeight() reflow
    old_setHeight = '''function setHeight(){
                var h = words[0].getBoundingClientRect().height;
                if(h > 0) kWrap.style.height = h + 'px';
                else kWrap.style.height = '1.1em';
            }'''
    new_setHeight = '''function setHeight(){
                requestAnimationFrame(function(){
                    var h = words[0].getBoundingClientRect().height;
                    if(h > 0) kWrap.style.height = h + 'px';
                    else kWrap.style.height = '1.1em';
                });
            }'''
    html = html.replace(old_setHeight, new_setHeight)
    
    # offsetHeight reflow
    html = html.replace(
        "window.addEventListener('load', function(){ if(_heroEl) _cachedHeroH = _heroEl.offsetHeight; });",
        "window.addEventListener('load', function(){ requestAnimationFrame(function(){ if(_heroEl) _cachedHeroH = _heroEl.offsetHeight; }); });"
    )
    html = html.replace(
        "window.addEventListener('resize', function(){ if(_heroEl) _cachedHeroH = _heroEl.offsetHeight; });",
        "window.addEventListener('resize', function(){ requestAnimationFrame(function(){ if(_heroEl) _cachedHeroH = _heroEl.offsetHeight; }); });"
    )

    # scrollHeight reflow
    html = html.replace(
        "window.addEventListener('load', function(){ _scrollMax = document.body.scrollHeight - window.innerHeight; });",
        "window.addEventListener('load', function(){ requestAnimationFrame(function(){ _scrollMax = document.body.scrollHeight - window.innerHeight; }); });"
    )
    html = html.replace(
        "window.addEventListener('resize', function(){ _scrollMax = document.body.scrollHeight - window.innerHeight; });",
        "window.addEventListener('resize', function(){ requestAnimationFrame(function(){ _scrollMax = document.body.scrollHeight - window.innerHeight; }); });"
    )

    # horizontal scroll hMaxT reflow
    old_hcalc = '''function _hCalc(){
                    var vH=window.innerHeight;
                    _hMaxT=Math.max(0,hTrack.scrollWidth-window.innerWidth+60);
                    hSection.style.height=(vH+_hMaxT*1.85)+'px';
                    _hScrollable=hSection.offsetHeight-vH;
                    _hSecTop=hSection.offsetTop;
                }'''
    new_hcalc = '''function _hCalc(){
                    requestAnimationFrame(function(){
                        var vH=window.innerHeight;
                        _hMaxT=Math.max(0,hTrack.scrollWidth-window.innerWidth+60);
                        hSection.style.height=(vH+_hMaxT*1.85)+'px';
                        _hScrollable=hSection.offsetHeight-vH;
                        _hSecTop=hSection.offsetTop;
                    });
                }'''
    html = html.replace(old_hcalc, new_hcalc)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(html)

print("Final PageSpeed optimizations applied.")
