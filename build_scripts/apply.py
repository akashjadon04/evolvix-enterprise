import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = '''        <!-- LAYER 1: BUSINESS CORE -->
        <div id="qstep-1" class="qstep" style="display:block;">
            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;text-align:center;">What best describes your architecture?</h3>
            <div class="grid-responsive-2">
                <button class="qbtn" onclick="window.auditEngine.select('btype', 'SaaS / Tech', this, 1, true)">
                    <div class="qbtn-icon">?</div>
                    <div><div class="qbtn-title">SaaS / Tech Product</div><div class="qbtn-sub">Software, apps, digital tools</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('btype', 'Agency / B2B', this, 1, true)">
                    <div class="qbtn-icon">??</div>
                    <div><div class="qbtn-title">Agency / B2B Services</div><div class="qbtn-sub">Consulting, freelancing, B2B</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('btype', 'Ecommerce', this, 1, true)">
                    <div class="qbtn-icon">???</div>
                    <div><div class="qbtn-title">E-commerce / D2C</div><div class="qbtn-sub">Physical or digital products</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('btype', 'Local Business', this, 1, true)">
                    <div class="qbtn-icon">??</div>
                    <div><div class="qbtn-title">Local / Service</div><div class="qbtn-sub">Restaurant, clinic, salon, etc.</div></div>
                </button>
            </div>
        </div>
        
        <!-- LAYER 2: REVENUE -->
        <div id="qstep-2" class="qstep" style="display:none;">
            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;text-align:center;">Current Monthly Revenue (MRR/Gross)</h3>
            <div class="grid-responsive-3">
                <button class="qbtn" style="padding:15px;justify-content:center;" onclick="window.auditEngine.select('rev', '< /mo', this, 2, true)"> - </button>
                <button class="qbtn" style="padding:15px;justify-content:center;" onclick="window.auditEngine.select('rev', '-/mo', this, 2, true)"> - </button>
                <button class="qbtn" style="padding:15px;justify-content:center;" onclick="window.auditEngine.select('rev', '+/mo', this, 2, true)">+</button>
            </div>
        </div>
        
        <!-- LAYER 3: BOTTLENECKS -->
        <div id="qstep-3" class="qstep" style="display:none;">
            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;text-align:center;">What is your primary bottleneck?</h3>
            <div style="display:grid;grid-template-columns:1fr;gap:16px;">
                <button class="qbtn" onclick="window.auditEngine.select('prob', 'Traffic & Leads', this, 3, true)">
                    <div class="qbtn-icon">??</div>
                    <div><div class="qbtn-title">Acquisition (Traffic & Leads)</div><div class="qbtn-sub">Not enough qualified people finding us</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('prob', 'Conversion & UX', this, 3, true)">
                    <div class="qbtn-icon">?</div>
                    <div><div class="qbtn-title">Conversion (UI/UX & Sales)</div><div class="qbtn-sub">People visit but don't convert into paying customers</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('prob', 'Systems & Tech', this, 3, true)">
                    <div class="qbtn-icon">??</div>
                    <div><div class="qbtn-title">Operations (Systems & Tech)</div><div class="qbtn-sub">Outdated tech, manual tasks, messy CRM</div></div>
                </button>
            </div>
        </div>

        <!-- LAYER 4: GOALS -->
        <div id="qstep-4" class="qstep" style="display:none;">
            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;text-align:center;">What is your target for the next 6 months?</h3>
            <div style="display:grid;grid-template-columns:1fr;gap:16px;">
                <button class="qbtn" onclick="window.auditEngine.select('goal', 'Double Revenue', this, 4, true)">
                    <div class="qbtn-icon">??</div>
                    <div><div class="qbtn-title">Aggressive Growth</div><div class="qbtn-sub">Double our revenue / 2x our traffic</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('goal', 'Automation & Scale', this, 4, true)">
                    <div class="qbtn-icon">??</div>
                    <div><div class="qbtn-title">Automate & Scale</div><div class="qbtn-sub">Reduce manual work, build custom software/apps</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('goal', 'Brand Authority', this, 4, true)">
                    <div class="qbtn-icon">??</div>
                    <div><div class="qbtn-title">Rebrand & Authority</div><div class="qbtn-sub">Look like a  enterprise, charge higher prices</div></div>
                </button>
            </div>
        </div>
        
        <!-- LAYER 5: IDENTITY -->
        <div id="qstep-5" class="qstep" style="display:none;">
            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;text-align:center;">Where should we send your Enterprise Report?</h3>
            <form onsubmit="event.preventDefault(); window.auditEngine.calculate();" class="grid-responsive-2">
                <input type="text" id="a-name" class="audit-input" placeholder="Your Name / Company Name" required>
                <input type="email" id="a-email" class="audit-input" placeholder="Your Work Email" required>
                <input type="tel" id="a-phone" class="audit-input" placeholder="WhatsApp / Phone Number" style="grid-column:1/-1;">
                <button type="submit" class="btn-cta-glow" style="grid-column:1/-1;width:100%;justify-content:center;margin-top:10px;">Generate Enterprise Report ?</button>
            </form>
        </div>
        
        <!-- LAYER LOAD: COMPUTING -->
        <div id="qstep-load" class="qstep" style="display:none;text-align:center;padding:40px 0;">
            <div style="margin:0 auto 30px;width:80px;height:80px;border:4px solid rgba(56,189,248,0.1);border-top-color:#38bdf8;border-radius:50%;animation:spinPulse 1.2s linear infinite;"></div>
            <h3 style="color:#fff;">Evolvix Core Computing Algorithm...</h3>
            <p style="color:#64748b;margin-top:10px;">Analyzing growth multipliers and formulating strategy</p>
        </div>
        
        <!-- LAYER FINAL: RESULTS -->
        <div id="qstep-final" class="qstep" style="display:none;">
            <div id="audit-results-final"></div>
        </div>

        </div></div></section>'''

# Replace HTML
# Find <!-- LAYER 1: IDENTITY --> up to </div></div></section> right before <!-- HIDDEN PDF TEMPLATE -->
pattern_html = r'<!-- LAYER 1: IDENTITY -->.*?</div></div></section>'
content = re.sub(pattern_html, new_html, content, flags=re.DOTALL, count=1)


# Replace JS
new_js = '''        select: function(key, val, btn, currentStep, autoNext = false) {
            this.answers[key] = val;
            var siblings = btn.parentElement.querySelectorAll('.qbtn');
            siblings.forEach(function(b){ b.classList.remove('selected'); });
            btn.classList.add('selected');
            
            if(autoNext) {
                var _this = this;
                setTimeout(function(){
                    document.getElementById('qstep-'+currentStep).style.display = 'none';
                    document.getElementById('qstep-'+(currentStep+1)).style.display = 'block';
                }, 300);
            }
        },
        calculate: function() {
            var name = document.getElementById('a-name').value;
            var email = document.getElementById('a-email').value;
            var phone = document.getElementById('a-phone').value;
            if(!name || !email) return;
            
            this.answers.name = name;
            this.answers.email = email;
            this.answers.phone = phone;
            
            if(!this.answers.goal || !this.answers.btype || !this.answers.prob) return;
            
            document.getElementById('qstep-5').style.display = 'none';
            document.getElementById('qstep-load').style.display = 'block';
            
            // Submit via FormSubmit natively
            try {
                var form = document.createElement('form');
                form.method = 'POST';
                form.action = 'https://api.web3forms.com/submit';
                var keyInput = document.createElement('input'); keyInput.type='hidden'; keyInput.name='access_key'; keyInput.value='453219ed-70bc-4e70-8b04-3be070c0f955'; form.appendChild(keyInput);
                
                var data = {
                    _subject: 'Enterprise Audit Lead: ' + name,
                    _captcha: 'false',
                    Name: name,
                    Email: email,
                    Phone: phone,
                    BusinessType: this.answers.btype,
                    Revenue: this.answers.rev,
                    Bottleneck: this.answers.prob,
                    TargetGoal: this.answers.goal
                };
                
                for (var k in data) {
                    var inp = document.createElement('input'); inp.type = 'hidden'; inp.name = k; inp.value = data[k]; form.appendChild(inp);
                }
                document.body.appendChild(form);
                form.submit();
            } catch(e) {}
            
            // Algorithm & Generate Results Layout similar to pricing.html
            var _this = this;
            setTimeout(function(){
                document.getElementById('qstep-load').style.display = 'none';
                document.getElementById('qstep-final').style.display = 'block';
                
                var score = Math.floor(Math.random() * 20) + 40; 
                if(_this.answers.rev === '+/mo') score += 20;
                if(_this.answers.prob === 'Systems & Tech') score -= 10;
                
                var sol = _this.answers.prob === 'Traffic & Leads' ? 'SEO & Viral Organic Growth Funnel' : 
                         (_this.answers.prob === 'Conversion & UX' ? 'Premium Web Design & Conversion Rate Optimization' : 'Custom SaaS & Workflow Automation Platform');
                         
                window.auditData = {
                    name: _this.answers.name,
                    btype: _this.answers.btype,
                    rev: _this.answers.rev,
                    neck: _this.answers.prob,
                    goal: _this.answers.goal
                };

                // Formatted just like pricing.html
                var html = '<div style="text-align:center;">';
                html += '<div style="font-size:0.85rem;color:#38bdf8;text-transform:uppercase;letter-spacing:2px;font-weight:700;margin-bottom:10px;">ENTERPRISE AUDIT COMPLETE</div>';
                html += '<h2 style="color:#fff;font-size:3.5rem;font-weight:900;margin-bottom:8px;">' + score + '<span style="font-size:1.5rem;color:#64748b;">/100</span></h2>';
                html += '<p style="color:#94a3b8;font-size:1.1rem;margin-bottom:20px;">Primary Bottleneck: <strong>' + _this.answers.prob + '</strong></p>';
                html += '<p style="color:#cbd5e1;margin-bottom:30px;max-width:500px;margin-left:auto;margin-right:auto;">Action Plan: Deploy a <strong>' + sol + '</strong> to achieve your goal of <strong>' + _this.answers.goal + '</strong>.</p>';
                html += '<a href="contact.html" class="btn-cta-glow" style="font-size:1.1rem;margin-bottom:15px;display:inline-flex;">Book Strategy Call to Execute Plan</a><br>';
                html += '<div style="margin-top:15px;"><button onclick="if(typeof window._buildPlaybookPDF === \\'function\\') { window._buildPlaybookPDF(); } else { alert(\\'Loading PDF engine, please click again in a moment.\\'); }" style="background:transparent;border:none;color:#67e8f9;text-decoration:underline;cursor:pointer;font-size:14px;padding:10px;">Download Executive Brief PDF</button></div>';
                html += '</div>';
                
                document.getElementById('audit-results-final').innerHTML = html;
                
                // Hide graphics on mobile when audit completes
                if(window.innerWidth <= 768) {
                    var hv = document.querySelector('.hero-visual');
                    if(hv) hv.style.display = 'none';
                }
            }, 5000);
        },'''

# Replace from 'select: function(key, val, btn, currentStep, autoNext = false) {' up to the exact start of 'downloadPDF: function() {'
pattern_js = r'select: function\(key, val, btn, currentStep, autoNext = false\) \{.*?downloadPDF: function\(\) \{'
content = re.sub(pattern_js, new_js + '\n        downloadPDF: function() {', content, flags=re.DOTALL, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
