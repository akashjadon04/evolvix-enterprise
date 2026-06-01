import codecs
import re
import os

def fix_index():
    with codecs.open('index.html', 'r', 'utf-8') as f:
        html = f.read()

    # 1. FIX SYNTAX ERRORS BREAKING SCROLL AND STATS
    html = html.replace("        })();\n\n        /* ─── Text Scramble On Hover ─── */", "        /* ─── Text Scramble On Hover ─── */")
    
    # Near line 1299
    html = html.replace("    })();\n        });\n    </script>", "    </script>")

    # 2. ADD FORM SUBMIT TO AUDIT
    # We injected window.auditEngine.calculate in V6.
    # Find `var email = document.getElementById('audit-email-v5').value;` and inject fetch.
    if 'fetch(\'https://formsubmit.co/ajax/evolvixtechnology@gmail.com\'' not in html:
        fetch_audit = r'''
            // Send to FormSubmit
            fetch('https://formsubmit.co/ajax/evolvixtechnology@gmail.com', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                body: JSON.stringify({
                    _subject: 'New Business Audit Lead',
                    Email: email,
                    BusinessType: this.answers.btype,
                    Bottleneck: this.answers.prob
                })
            }).catch(e => console.error(e));
        '''
        html = html.replace("document.getElementById('qstep-3').style.display = 'none';", 
                            "document.getElementById('qstep-3').style.display = 'none';" + fetch_audit)

    # 3. FIX PLAYBOOK MODAL SUBMIT
    # Ensure downloadPlaybook is defined
    if 'function downloadPlaybook()' not in html:
        playbook_js = '''
    <script>
    function downloadPlaybook() {
        var email = document.getElementById('playbook-email').value;
        if(!email) return;
        var btn = document.querySelector('#playbookModal button[type="submit"]');
        btn.textContent = 'Sending...';
        btn.style.pointerEvents = 'none';
        
        fetch('https://formsubmit.co/ajax/evolvixtechnology@gmail.com', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
            body: JSON.stringify({
                _subject: 'Playbook Download Request',
                Email: email
            })
        }).then(res => {
            btn.textContent = 'Sent! Check Email.';
            setTimeout(() => { document.getElementById('playbookModal').style.display = 'none'; }, 2000);
        }).catch(e => {
            btn.textContent = 'Error. Try again.';
            btn.style.pointerEvents = 'all';
        });
    }
    </script>
    '''
        html = html.replace('</body>', playbook_js + '\n</body>')

    # 4. FIX HERO ANIMATIONS CSS
    # Add default hidden state for stagger children so IntersectionObserver works
    if '.stagger-child { opacity: 0' not in html:
        stagger_css = '''
    <style>
    .stagger-child {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .stagger-child.visible {
        opacity: 1;
        transform: translateY(0);
    }
    </style>
    </head>'''
        html = html.replace('</head>', stagger_css)

    with codecs.open('index.html', 'w', 'utf-8') as f:
        f.write(html)
    print("index.html fixed (Syntax, Audit Form, Playbook Form, Stagger CSS).")

def fix_pricing():
    if not os.path.exists('pricing.html'): return
    with codecs.open('pricing.html', 'r', 'utf-8') as f:
        html = f.read()

    if 'fetch(\'https://formsubmit.co/ajax/evolvixtechnology@gmail.com\'' not in html:
        fetch_pricing = r'''
                // Send to FormSubmit
                fetch('https://formsubmit.co/ajax/evolvixtechnology@gmail.com', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                    body: JSON.stringify({
                        _subject: 'New Pricing Estimate Request',
                        Name: name,
                        Email: email,
                        Service: this.answers.service,
                        Scale: this.answers.scale,
                        Timeline: this.answers.time
                    })
                }).catch(e => console.error(e));
        '''
        html = html.replace("document.getElementById('est-step-4').style.display='none';",
                            "document.getElementById('est-step-4').style.display='none';" + fetch_pricing)
        
        with codecs.open('pricing.html', 'w', 'utf-8') as f:
            f.write(html)
        print("pricing.html fixed (FormSubmit).")

def fix_contact():
    if not os.path.exists('contact.html'): return
    with codecs.open('contact.html', 'r', 'utf-8') as f:
        html = f.read()
    
    html = html.replace('usawebmastersdrip@gmail.com', 'evolvixtechnology@gmail.com')
    
    with codecs.open('contact.html', 'w', 'utf-8') as f:
        f.write(html)
    print("contact.html fixed (FormSubmit email).")

def fix_script_js():
    with codecs.open('script.js', 'r', 'utf-8') as f:
        js = f.read()

    # 1. OPTIMIZE PHYSICS WORLD (Fix PageSpeed Drop)
    # Replace particle count logic
    js = js.replace('this.particleCount=window.innerWidth<768?12:35', 'this.particleCount=window.innerWidth<768?8:15')
    
    # Remove O(N^2) line drawing
    line_draw_pattern = r'for\(let s=t;s<this\.particles\.length;s\+\+\)\{.*?\}\}'
    js = re.sub(line_draw_pattern, '}', js, flags=re.DOTALL)

    # 2. UPGRADE CURSOR WITH TRAILS
    # Remove old cursor logic first
    js = re.sub(r'/\* ─── Premium Magnetic Cursor ─── \*/.*?\}\)\(\);', '', js, flags=re.DOTALL)
    
    # Add new beautiful trailing cursor
    trailing_cursor_js = '''
/* ─── Premium Magnetic Trailing Cursor ─── */
(function(){
    if(!window.matchMedia('(pointer:fine)').matches) return; // Only desktop
    
    // Main cursor dot
    var c=document.createElement('div');
    c.style.cssText='position:fixed;top:0;left:0;width:8px;height:8px;background:#38bdf8;border-radius:50%;pointer-events:none;z-index:999999;transform:translate(-50%,-50%);transition:transform 0.1s;';
    document.body.appendChild(c);

    // Trail elements
    var trails = [];
    var numTrails = 6;
    for(var i=0; i<numTrails; i++) {
        var t = document.createElement('div');
        t.style.cssText=`position:fixed;top:0;left:0;width:${24 - i*3}px;height:${24 - i*3}px;border:1px solid rgba(56,189,248,${0.6 - i*0.1});border-radius:50%;pointer-events:none;z-index:${999998-i};transform:translate(-50%,-50%);`;
        document.body.appendChild(t);
        trails.push({el: t, x: -100, y: -100});
    }
    
    var mx=-100, my=-100;
    var hovered = false;

    window.addEventListener('mousemove', function(e){
        mx = e.clientX; my = e.clientY;
        c.style.left = mx+'px'; 
        c.style.top = my+'px';
    });
    
    function loop(){
        var tx = mx, ty = my;
        for(var i=0; i<numTrails; i++){
            var tr = trails[i];
            tr.x += (tx - tr.x) * (0.3 - i*0.02);
            tr.y += (ty - tr.y) * (0.3 - i*0.02);
            tr.el.style.left = tr.x + 'px';
            tr.el.style.top = tr.y + 'px';
            tx = tr.x; ty = tr.y; // Next trail follows this one
            
            if(hovered) {
                tr.el.style.background = `rgba(56,189,248,${0.1 - i*0.01})`;
                tr.el.style.transform = `translate(-50%,-50%) scale(1.5)`;
            } else {
                tr.el.style.background = 'transparent';
                tr.el.style.transform = `translate(-50%,-50%) scale(1)`;
            }
        }
        requestAnimationFrame(loop);
    }
    loop();
    
    function attach(){
        document.querySelectorAll('a, button, .qbtn, input, .wiz-btn, .premium-btn, .btn').forEach(function(el){
            if(el.dataset.tc) return;
            el.dataset.tc = '1';
            el.addEventListener('mouseenter', ()=>hovered=true);
            el.addEventListener('mouseleave', ()=>hovered=false);
        });
    }
    attach(); setInterval(attach, 1500);
})();
'''
    js += "\n" + trailing_cursor_js

    with codecs.open('script.js', 'w', 'utf-8') as f:
        f.write(js)
    print("script.js fixed (Physics Optimization, Cursor Trails).")

if __name__ == '__main__':
    fix_index()
    fix_pricing()
    fix_contact()
    fix_script_js()
