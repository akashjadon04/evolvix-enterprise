import re
import codecs
import os
import glob

def fix_index():
    with codecs.open('index.html', 'r', 'utf-8') as f:
        html = f.read()

    # 1. FIX WHATSAPP
    html = html.replace('right:30px', 'left:30px').replace('right: 30px', 'left: 30px')
    html = html.replace('917999863831', '917668758238')
    
    # 2. START PROJECT BUTTONS GLOW & STYLE
    glow_css = '''
    <style>
    .btn-cta-glow {
        position: relative;
        background-image: linear-gradient(45deg, #38bdf8 0%, #818cf8 50%, #38bdf8 100%);
        background-size: 200% auto;
        color: #fff !important;
        border: none;
        border-radius: 30px;
        font-weight: 800;
        letter-spacing: 0.5px;
        padding: 0.8rem 1.8rem !important;
        overflow: hidden;
        z-index: 1;
        transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 4px 15px rgba(56, 189, 248, 0.4), inset 0 1px 0 rgba(255,255,255,0.4);
        display: inline-flex;
        align-items: center;
        text-decoration: none;
    }
    .btn-cta-glow:hover {
        background-position: right center;
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 12px 25px rgba(56, 189, 248, 0.6), inset 0 1px 0 rgba(255,255,255,0.6);
    }
    .btn-cta-glow .btn-arrow { display: inline-block; transition: transform 0.3s; margin-left: 6px; }
    .btn-cta-glow:hover .btn-arrow { transform: translateX(4px); }
    </style>
    </head>'''
    if '.btn-cta-glow' not in html:
        html = html.replace('</head>', glow_css)
    else:
        # Update existing css if any
        pass

    # Replace old buttons
    html = re.sub(
        r'<a href="contact\.html" class="btn btn-primary"[^>]*>.*?Start Project.*?</a>',
        '<a href="contact.html" class="btn btn-primary btn-cta-glow">Start Project <span class="btn-arrow">→</span></a>',
        html,
        flags=re.DOTALL
    )

    # 3. AUDIT ENGINE REWRITE
    new_audit_html = r'''<section class="section" id="audit" style="position: relative; z-index: 10; overflow: hidden; padding: 100px 0;">
            <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 100%; max-width: 1200px; height: 100%; pointer-events: none; z-index: -1;">
                <div style="position: absolute; top: -10%; right: 10%; width: 400px; height: 400px; background: radial-gradient(circle, rgba(56,189,248,0.1) 0%, transparent 70%); border-radius: 50%;"></div>
                <div style="position: absolute; bottom: 0; left: 10%; width: 600px; height: 600px; background: radial-gradient(circle, rgba(139,92,246,0.05) 0%, transparent 70%); border-radius: 50%;"></div>
            </div>
            
            <div class="container">
                <div class="form-card reveal" style="max-width:850px; margin:0 auto; padding:60px; background:rgba(15,23,42,0.7); backdrop-filter:blur(20px); border:1px solid rgba(56,189,248,0.2); border-radius:24px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);">
                    <div style="text-align:center; margin-bottom:40px;">
                        <span style="background:linear-gradient(90deg, rgba(56,189,248,0.1), rgba(139,92,246,0.1)); border: 1px solid rgba(56,189,248,0.3); color:#38bdf8; padding:8px 24px; border-radius:30px; font-size:0.85rem; font-weight:700; letter-spacing: 2px; text-transform: uppercase;">Evolvix Core Intelligence</span>
                        <h2 style="color:#fff !important; font-size:3rem; font-weight: 800; letter-spacing: -1px; margin-top:25px; line-height: 1.2;">Uncover Your Growth Bottlenecks</h2>
                    </div>

        <style>
        .qstep { animation: qFadeIn 0.5s cubic-bezier(0.2, 0.8, 0.2, 1); }
        @keyframes qFadeIn { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }
        
        .qbtn { 
            display:flex; align-items:center; gap:18px; 
            background:rgba(15, 23, 42, 0.4); border:1px solid rgba(56,189,248,0.15); 
            color:#f8fafc; border-radius:16px; padding:20px; cursor:pointer; 
            transition:all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); text-align:left; width:100%;
            position: relative; overflow: hidden;
            backdrop-filter: blur(10px);
        }
        .qbtn::before {
            content: ''; position: absolute; top: 0; left: -100%; width: 50%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
            transform: skewX(-20deg); transition: 0.5s;
        }
        .qbtn:hover::before { left: 150%; }
        .qbtn:hover { background:rgba(56,189,248,0.08); border-color:rgba(56,189,248,0.5); transform:translateY(-4px); box-shadow:0 12px 30px -10px rgba(56,189,248,0.3); }
        .qbtn.selected { background:rgba(56,189,248,0.15); border-color:#38bdf8; box-shadow:0 0 0 1px #38bdf8 inset, 0 10px 30px -10px rgba(56,189,248,0.4); }
        
        .qbtn-icon { font-size:1.8rem; flex-shrink:0; width:48px; height: 48px; background: rgba(255,255,255,0.03); border-radius: 12px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.05); }
        .qbtn-title { font-size:1.05rem; font-weight:700; color:#fff; margin-bottom:4px; letter-spacing: 0.3px; }
        .qbtn-sub { font-size:0.85rem; color:#94a3b8; }
        @keyframes spinPulse { 0% {transform:rotate(0deg); border-top-color:#38bdf8;} 50% {border-top-color:#818cf8;} 100% {transform:rotate(360deg); border-top-color:#38bdf8;} }
        </style>
        
        <div id="qstep-1" class="qstep">
            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;text-align:center;">What best describes your business?</h3>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
                <button class="qbtn" onclick="window.auditEngine.select('btype', 'SaaS', this)">
                    <div class="qbtn-icon">⚡</div>
                    <div><div class="qbtn-title">SaaS / Tech Product</div><div class="qbtn-sub">Software, apps, digital tools</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('btype', 'Agency', this)">
                    <div class="qbtn-icon">🎯</div>
                    <div><div class="qbtn-title">Agency / B2B Services</div><div class="qbtn-sub">Consulting, freelancing, B2B</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('btype', 'Ecommerce', this)">
                    <div class="qbtn-icon">🛍️</div>
                    <div><div class="qbtn-title">E-commerce / D2C Brand</div><div class="qbtn-sub">Physical or digital products</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('btype', 'Local', this)">
                    <div class="qbtn-icon">📍</div>
                    <div><div class="qbtn-title">Local / Service Business</div><div class="qbtn-sub">Restaurant, clinic, salon, etc.</div></div>
                </button>
            </div>
        </div>
        
        <div id="qstep-2" class="qstep" style="display:none;">
            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;text-align:center;">What is your biggest current bottleneck?</h3>
            <div style="display:grid;grid-template-columns:1fr;gap:16px;">
                <button class="qbtn" onclick="window.auditEngine.select('prob', 'Traffic', this)">
                    <div class="qbtn-icon">📉</div>
                    <div><div class="qbtn-title">Not enough traffic or leads</div><div class="qbtn-sub">Struggling to get visibility online</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('prob', 'Conversion', this)">
                    <div class="qbtn-icon">💔</div>
                    <div><div class="qbtn-title">Traffic isn't converting</div><div class="qbtn-sub">People visit but don't buy or contact</div></div>
                </button>
                <button class="qbtn" onclick="window.auditEngine.select('prob', 'Systems', this)">
                    <div class="qbtn-icon">⚙️</div>
                    <div><div class="qbtn-title">Operations & systems are a mess</div><div class="qbtn-sub">Need better tech, CRM, or automation</div></div>
                </button>
            </div>
        </div>
        
        <div id="qstep-3" class="qstep" style="display:none;">
            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;text-align:center;">Generate Your Business Audit</h3>
            <form id="audit-form-v5" onsubmit="event.preventDefault(); window.auditEngine.calculate();" style="display:flex;flex-direction:column;gap:16px;max-width:400px;margin:0 auto;">
                <input id="audit-email-v5" type="email" placeholder="Enter your best email" required style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.1);color:#fff;padding:18px;border-radius:14px;font-size:1rem;outline:none;" onfocus="this.style.borderColor='#38bdf8'" onblur="this.style.borderColor='rgba(255,255,255,0.1)'">
                <button type="submit" class="btn-cta-glow" style="width:100%;justify-content:center;">Run Diagnostic & Get Results →</button>
            </form>
        </div>
        
        <div id="qstep-4" class="qstep" style="display:none;text-align:center;padding:40px 0;">
            <div style="margin:0 auto 30px;width:80px;height:80px;border:4px solid rgba(56,189,248,0.1);border-top-color:#38bdf8;border-radius:50%;animation:spinPulse 1.2s linear infinite;"></div>
            <h3 style="color:#fff;">Evolvix Core Computing Algorithm...</h3>
            <p style="color:#64748b;margin-top:10px;">Analyzing growth multipliers</p>
        </div>
        
        <div id="qstep-5" class="qstep" style="display:none;">
            <div id="audit-results-v5"></div>
            
            <div style="text-align:center; margin-top:30px;">
                <button onclick="window.auditEngine.downloadPDF()" class="btn-cta-glow" style="background-image:linear-gradient(45deg, #22c55e 0%, #16a34a 50%, #22c55e 100%);">📥 Download Enterprise Strategy PDF</button>
            </div>
        </div>

        </div></div></section>
        
        <!-- HIDDEN PDF TEMPLATE -->
        <div id="hidden-pdf-template" style="display:none; padding:40px; background:#fff; color:#0f172a; font-family:'Outfit',sans-serif; width:800px;">
            <div style="border-bottom:4px solid #38bdf8; padding-bottom:20px; margin-bottom:30px; display:flex; justify-content:space-between; align-items:center;">
                <h1 style="margin:0; font-size:32px; color:#0f172a;">Evolvix Technologies</h1>
                <span style="font-weight:700; color:#64748b; font-size:14px;">ENTERPRISE STRATEGY AUDIT</span>
            </div>
            
            <div style="display:flex; justify-content:space-between; margin-bottom:40px;">
                <div style="background:#f8fafc; padding:20px; border-radius:12px; border:1px solid #e2e8f0; width:48%;">
                    <p style="margin:0 0 5px; color:#64748b; font-size:12px; font-weight:700; text-transform:uppercase;">Business Profile</p>
                    <h3 style="margin:0; font-size:24px;" id="pdf-btype">SaaS</h3>
                </div>
                <div style="background:#f8fafc; padding:20px; border-radius:12px; border:1px solid #e2e8f0; width:48%;">
                    <p style="margin:0 0 5px; color:#64748b; font-size:12px; font-weight:700; text-transform:uppercase;">Health Score</p>
                    <h3 style="margin:0; font-size:24px; color:#ef4444;" id="pdf-score">45/100</h3>
                </div>
            </div>
            
            <h2 style="border-bottom:1px solid #e2e8f0; padding-bottom:10px; margin-bottom:20px;">Primary Bottleneck Analysis</h2>
            <p style="font-size:18px; line-height:1.6; color:#334155; margin-bottom:40px;" id="pdf-analysis"></p>
            
            <h2 style="border-bottom:1px solid #e2e8f0; padding-bottom:10px; margin-bottom:20px;">Action Plan & Solution</h2>
            <div style="background:#e0f2fe; border-left:4px solid #38bdf8; padding:20px; margin-bottom:40px;">
                <h3 style="margin:0 0 10px; color:#0284c7;" id="pdf-sol">SEO</h3>
                <p style="margin:0; color:#0c4a6e; font-size:16px;" id="pdf-roi">ROI: 3x Traffic</p>
            </div>
            
            <div style="margin-top:60px; padding-top:20px; border-top:1px solid #e2e8f0; display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <img src="https://upload.wikimedia.org/wikipedia/commons/1/14/Signature_Placeholder.png" style="height:50px; opacity:0.8; mix-blend-mode:multiply; filter: grayscale(100%);" alt="Akash Signature">
                    <p style="margin:5px 0 0; font-weight:700;">Akash Jadon</p>
                    <p style="margin:0; font-size:12px; color:#64748b;">CEO, Evolvix Technologies</p>
                </div>
                <div style="text-align:right;">
                    <p style="margin:0; font-weight:700; color:#38bdf8;">evolvixtechnology@gmail.com</p>
                    <p style="margin:0; font-size:14px; color:#64748b;">+91 7668758238</p>
                </div>
            </div>
        </div>

    <script id="audit-engine">
    window.auditEngine = {
        answers: {},
        select: function(key, val, btn) {
            this.answers[key] = val;
            var siblings = btn.parentElement.querySelectorAll('.qbtn');
            siblings.forEach(function(b){ b.classList.remove('selected'); b.style.pointerEvents='none'; });
            btn.classList.add('selected');
            
            var step = key === 'btype' ? 1 : 2;
            setTimeout(function(){
                document.getElementById('qstep-'+step).style.display = 'none';
                document.getElementById('qstep-'+(step+1)).style.display = 'block';
            }, 300);
        },
        calculate: function() {
            var email = document.getElementById('audit-email-v5').value;
            if(!email) return;
            document.getElementById('qstep-3').style.display = 'none';
            document.getElementById('qstep-4').style.display = 'block';
            
            var _this = this;
            setTimeout(function(){
                document.getElementById('qstep-4').style.display = 'none';
                document.getElementById('qstep-5').style.display = 'block';
                
                var score = _this.answers.prob === 'Traffic' ? 45 : (_this.answers.prob === 'Conversion' ? 60 : 75);
                var sol = _this.answers.prob === 'Traffic' ? 'SEO & Organic Growth Engine' : (_this.answers.prob === 'Conversion' ? 'Premium Web Design & CRO' : 'Custom SaaS / Automation Platform');
                var roi = _this.answers.prob === 'Traffic' ? '3x Traffic Growth' : (_this.answers.prob === 'Conversion' ? '+150% Conversion Rate' : '-40% Operational Time');
                
                var html = '<div style="background:rgba(15,23,42,0.7);backdrop-filter:blur(15px);border:1px solid rgba(56,189,248,0.2);border-radius:20px;padding:30px;">';
                html += '<div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:20px;margin-bottom:20px;">';
                html += '<div><h4 style="color:#94a3b8;font-size:0.9rem;margin:0 0 5px;">BUSINESS HEALTH SCORE</h4>';
                html += '<h2 style="color:#38bdf8;font-size:3rem;margin:0;font-weight:900;">' + score + '<span style="font-size:1.5rem;color:#64748b;">/100</span></h2></div>';
                html += '</div>';
                
                html += '<h4 style="color:#fff;margin:0 0 10px;font-size:1.2rem;">Diagnosis:</h4>';
                html += '<p style="color:#cbd5e1;margin:0 0 20px;">Your ' + _this.answers.btype + ' business is currently bottlenecked by <strong>' + _this.answers.prob.toLowerCase() + '</strong> issues. This indicates a critical failure point in your scaling architecture.</p>';
                
                html += '<div style="background:rgba(56,189,248,0.05);border:1px solid rgba(56,189,248,0.15);padding:20px;border-radius:12px;margin-bottom:25px;">';
                html += '<h4 style="color:#38bdf8;margin:0 0 10px;">Recommended Action Plan</h4>';
                html += '<ul style="color:#f1f5f9;margin:0;padding-left:20px;line-height:1.6;">';
                html += '<li>Implement a <strong>' + sol + '</strong></li>';
                html += '<li>Fix core UI/UX and system architectures</li>';
                html += '<li>Expected Impact: <span style="color:#22c55e;font-weight:bold;">' + roi + '</span></li>';
                html += '</ul></div>';
                
                html += '<div style="text-align:center;"><a href="contact.html" class="btn-cta-glow" style="width:100%;justify-content:center;">Book Strategy Call to Execute Plan →</a></div>';
                html += '</div>';
                
                document.getElementById('audit-results-v5').innerHTML = html;
                
                // Set PDF template data
                document.getElementById('pdf-btype').innerText = _this.answers.btype + ' Industry';
                document.getElementById('pdf-score').innerText = score + '/100 (Critical)';
                document.getElementById('pdf-analysis').innerText = 'Based on our proprietary diagnostic algorithm, your primary bottleneck is ' + _this.answers.prob + '. This is restricting your revenue flow and capping your operational scale.';
                document.getElementById('pdf-sol').innerText = 'Recommendation: ' + sol;
                document.getElementById('pdf-roi').innerText = 'Expected Outcome: ' + roi;
                
            }, 5000); // 5 second delay to build curiosity
        },
        downloadPDF: function() {
            var el = document.getElementById('hidden-pdf-template');
            el.style.display = 'block'; // unhide temporarily
            var opt = {
              margin:       0.5,
              filename:     'Evolvix_Strategy_Audit.pdf',
              image:        { type: 'jpeg', quality: 0.98 },
              html2canvas:  { scale: 2, useCORS: true },
              jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
            };
            html2pdf().set(opt).from(el).save().then(function(){
                el.style.display = 'none';
            });
        }
    };
    </script>'''
    
    html = re.sub(r'<section class="section" id="audit".*?</section>', new_audit_html, html, flags=re.DOTALL)


    # 4. EXIT INTENT POPUP (No timer, only popstate)
    html = re.sub(r'setTimeout\(\(\)\s*=>\s*\{\s*const pm\s*=\s*document\.getElementById\(\'playbookModal\'\);.*?\},\s*30000\);', '', html, flags=re.DOTALL)
    
    exit_intent_js = '''
    <script>
    document.addEventListener('DOMContentLoaded', () => {
        // Push a dummy state so back button works
        window.history.pushState({page: 1}, "Evolvix", "");
        
        window.addEventListener('popstate', function(event) {
            const pm = document.getElementById('playbookModal');
            if(pm && pm.style.display !== 'flex') {
                pm.style.display = 'flex';
                // Push state back so they don't actually leave if they dismiss it
                window.history.pushState({page: 1}, "Evolvix", "");
            }
        });
    });
    </script>
    </body>
    '''
    # Only add once
    if 'popstate' not in html:
        html = html.replace('</body>', exit_intent_js)
    
    with codecs.open('index.html', 'w', 'utf-8') as f:
        f.write(html)
    print('index.html V6 fixed!')


def fix_pricing():
    with codecs.open('pricing.html', 'r', 'utf-8') as f:
        html = f.read()

    # Rebuild the main section for pricing
    new_pricing = '''<main>
        <!-- PRICING HERO -->
        <section class="section text-center" style="min-height:40vh;display:flex;align-items:center;justify-content:center;padding:120px 0 40px;">
            <div class="container">
                <div class="reveal">
                    <span style="display:inline-block;background:linear-gradient(90deg,rgba(56,189,248,0.12),rgba(139,92,246,0.12));border:1px solid rgba(56,189,248,0.25);color:#38bdf8;padding:8px 24px;border-radius:30px;font-size:0.8rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;margin-bottom:24px;">Project Estimator</span>
                    <h1 style="font-size:clamp(3rem,8vw,5.5rem);font-weight:900;letter-spacing:-2px;line-height:1.05;margin-bottom:20px;font-family:'Outfit', sans-serif;">
                        Transparent Pricing.<br><span class="text-gradient">No Surprises.</span>
                    </h1>
                </div>
            </div>
        </section>

        <!-- PRICING ESTIMATOR WIZARD -->
        <section class="section" style="padding-top:0;padding-bottom:120px;">
            <div class="container">
                <div style="max-width:900px;margin:0 auto;background:rgba(15,23,42,0.6);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid rgba(56,189,248,0.2);border-radius:32px;overflow:hidden;box-shadow:0 40px 100px -20px rgba(0,0,0,0.7);" class="reveal">
                    
                    <div style="padding:56px 64px;" id="pricing-wizard">

                        <style>
                        .qstep { animation: qFadeIn 0.5s cubic-bezier(0.2, 0.8, 0.2, 1); }
                        @keyframes qFadeIn { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }
                        .qbtn { display:flex; align-items:center; gap:18px; background:rgba(15, 23, 42, 0.4); border:1px solid rgba(56,189,248,0.15); color:#f8fafc; border-radius:16px; padding:20px; cursor:pointer; transition:all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); text-align:left; width:100%; position: relative; overflow: hidden; }
                        .qbtn:hover { background:rgba(56,189,248,0.08); border-color:rgba(56,189,248,0.5); transform:translateY(-4px); box-shadow:0 12px 30px -10px rgba(56,189,248,0.3); }
                        .qbtn.selected { background:rgba(56,189,248,0.15); border-color:#38bdf8; box-shadow:0 0 0 1px #38bdf8 inset, 0 10px 30px -10px rgba(56,189,248,0.4); }
                        .qbtn-icon { font-size:1.8rem; flex-shrink:0; width:48px; height: 48px; background: rgba(255,255,255,0.03); border-radius: 12px; display: flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,0.05); }
                        .qbtn-title { font-size:1.05rem; font-weight:700; color:#fff; margin-bottom:4px; letter-spacing: 0.3px; }
                        .qbtn-sub { font-size:0.85rem; color:#94a3b8; }
                        @keyframes spinPulse { 0% {transform:rotate(0deg); border-top-color:#38bdf8;} 50% {border-top-color:#818cf8;} 100% {transform:rotate(360deg); border-top-color:#38bdf8;} }
                        </style>

                        <!-- STEP 1: Service Type -->
                        <div class="qstep" id="est-step-1">
                            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;">1. What type of project are you building?</h3>
                            <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
                                <button class="qbtn" onclick="window.pricingEngine.select('service', 'site', this)">
                                    <div class="qbtn-icon">🖥️</div><div><div class="qbtn-title">High-Performance Website</div><div class="qbtn-sub">Marketing site, landing pages</div></div>
                                </button>
                                <button class="qbtn" onclick="window.pricingEngine.select('service', 'saas', this)">
                                    <div class="qbtn-icon">⚡</div><div><div class="qbtn-title">Custom SaaS / Web App</div><div class="qbtn-sub">Complex logic, dashboards</div></div>
                                </button>
                                <button class="qbtn" onclick="window.pricingEngine.select('service', 'ecom', this)">
                                    <div class="qbtn-icon">🛍️</div><div><div class="qbtn-title">E-Commerce Platform</div><div class="qbtn-sub">Online store, payments</div></div>
                                </button>
                                <button class="qbtn" onclick="window.pricingEngine.select('service', 'seo', this)">
                                    <div class="qbtn-icon">📈</div><div><div class="qbtn-title">SEO & Lead Generation</div><div class="qbtn-sub">Local SEO, funnels, automation</div></div>
                                </button>
                            </div>
                        </div>

                        <!-- STEP 2: Scale/Features -->
                        <div class="qstep" id="est-step-2" style="display:none;">
                            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;">2. What is the scale of the project?</h3>
                            <div style="display:grid;grid-template-columns:1fr;gap:16px;">
                                <button class="qbtn" onclick="window.pricingEngine.select('scale', 'mvp', this)">
                                    <div class="qbtn-icon">🌱</div><div><div class="qbtn-title">MVP / Foundation</div><div class="qbtn-sub">Essential features, standard design, fast launch.</div></div>
                                </button>
                                <button class="qbtn" onclick="window.pricingEngine.select('scale', 'growth', this)">
                                    <div class="qbtn-icon">🚀</div><div><div class="qbtn-title">Growth Grade (Most Popular)</div><div class="qbtn-sub">Custom premium design, advanced animations.</div></div>
                                </button>
                                <button class="qbtn" onclick="window.pricingEngine.select('scale', 'enterprise', this)">
                                    <div class="qbtn-icon">👑</div><div><div class="qbtn-title">Enterprise Scale</div><div class="qbtn-sub">Complex 3D/WebGL, custom backend architecture.</div></div>
                                </button>
                            </div>
                        </div>

                        <!-- STEP 3: Timeline -->
                        <div class="qstep" id="est-step-3" style="display:none;">
                            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;">3. When do you need this launched?</h3>
                            <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
                                <button class="qbtn" onclick="window.pricingEngine.select('time', 'asap', this)">
                                    <div class="qbtn-icon">🔥</div><div><div class="qbtn-title">ASAP (Priority)</div><div class="qbtn-sub">Rush Delivery</div></div>
                                </button>
                                <button class="qbtn" onclick="window.pricingEngine.select('time', 'normal', this)">
                                    <div class="qbtn-icon">📅</div><div><div class="qbtn-title">Standard Timeline</div><div class="qbtn-sub">1 to 2 months</div></div>
                                </button>
                                <button class="qbtn" onclick="window.pricingEngine.select('time', 'flex', this)">
                                    <div class="qbtn-icon">🧘‍♂️</div><div><div class="qbtn-title">Flexible</div><div class="qbtn-sub">3+ months</div></div>
                                </button>
                            </div>
                        </div>

                        <!-- STEP 4: Form -->
                        <div class="qstep" id="est-step-4" style="display:none;">
                            <h3 style="color:#fff;font-size:1.8rem;margin-bottom:24px;">4. Generate Your Estimate</h3>
                            <form onsubmit="event.preventDefault(); window.pricingEngine.calculate();" style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
                                <input id="est-name" type="text" placeholder="Full Name" required style="grid-column:1/2;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.1);color:#fff;padding:18px;border-radius:14px;font-size:1rem;outline:none;">
                                <input id="est-email" type="email" placeholder="Work Email" required style="grid-column:2/3;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.1);color:#fff;padding:18px;border-radius:14px;font-size:1rem;outline:none;">
                                <button type="submit" class="btn-cta-glow" style="grid-column:1/-1;width:100%;justify-content:center;">Calculate Investment →</button>
                            </form>
                        </div>
                        
                        <!-- STEP LOADING -->
                        <div class="qstep" id="est-step-load" style="display:none;text-align:center;padding:60px 0;">
                            <div style="margin:0 auto 30px;width:80px;height:80px;border:4px solid rgba(56,189,248,0.1);border-top-color:#38bdf8;border-radius:50%;animation:spinPulse 1.2s linear infinite;"></div>
                            <h3 style="color:#fff;font-size:1.8rem;font-weight:800;">Generating Custom Proposal...</h3>
                            <p style="color:#64748b;margin-top:10px;">Estimating resource allocation and timelines</p>
                        </div>

                        <!-- STEP 5: Results -->
                        <div class="qstep" id="est-step-5" style="display:none;">
                            <div id="est-results"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <script>
        window.pricingEngine = {
            answers: {},
            select: function(key, val, btn) {
                this.answers[key] = val;
                var siblings = btn.parentElement.querySelectorAll('.qbtn');
                siblings.forEach(function(b){ b.classList.remove('selected'); b.style.pointerEvents='none'; });
                btn.classList.add('selected');
                var map = {service: 1, scale: 2, time: 3};
                var step = map[key];
                setTimeout(function(){
                    document.getElementById('est-step-'+step).style.display='none';
                    document.getElementById('est-step-'+(step+1)).style.display='block';
                }, 300);
            },
            calculate: function() {
                var name = document.getElementById('est-name').value;
                var email = document.getElementById('est-email').value;
                if(!name || !email) return;
                
                document.getElementById('est-step-4').style.display='none';
                document.getElementById('est-step-load').style.display='block';
                
                // 30% Lower base pricing 
                // Old base=20000 -> New base=14000
                var base = 14000; var max = 24500; var title = "High-Performance Website";
                if(this.answers.service === 'saas') { base = 42000; max = 105000; title = "Custom SaaS Platform"; }
                if(this.answers.service === 'ecom') { base = 31500; max = 56000; title = "E-Commerce Solution"; }
                if(this.answers.service === 'seo') { base = 10500; max = 21000; title = "Growth & SEO Campaign (Monthly)"; }
                
                if(this.answers.scale === 'growth') { base *= 1.5; max *= 1.5; }
                if(this.answers.scale === 'enterprise') { base *= 2.5; max *= 3.0; }
                if(this.answers.time === 'asap') { base *= 1.3; max *= 1.3; }
                
                var format = function(n){ return '₹' + Math.round(n).toLocaleString('en-IN'); };
                var str = format(base) + ' — ' + format(max);
                if(this.answers.service === 'seo') str += ' / mo';
                
                var html = '<div style="text-align:center;">';
                html += '<div style="font-size:0.85rem;color:#38bdf8;text-transform:uppercase;letter-spacing:2px;font-weight:700;margin-bottom:10px;">ESTIMATE GENERATED</div>';
                html += '<h2 style="color:#fff;font-size:2.5rem;font-weight:900;margin-bottom:8px;">' + str + '</h2>';
                html += '<p style="color:#94a3b8;font-size:1.1rem;margin-bottom:30px;">For: ' + title + '</p>';
                html += '<a href="contact.html" class="btn-cta-glow" style="font-size:1.1rem;">Book Strategy Call to Finalize Scope →</a>';
                html += '</div>';
                
                setTimeout(function(){
                    document.getElementById('est-step-load').style.display='none';
                    document.getElementById('est-step-5').style.display='block';
                    document.getElementById('est-results').innerHTML = html;
                }, 5000); // 5 seconds curiosity delay
            }
        };
        </script>
    </main>'''
    
    html = re.sub(r'<main>.*?</main>', new_pricing, html, flags=re.DOTALL)
    
    # Glow button CSS in pricing
    glow_css = '''
    <style>
    .btn-cta-glow {
        position: relative; background-image: linear-gradient(45deg, #38bdf8 0%, #818cf8 50%, #38bdf8 100%);
        background-size: 200% auto; color: #fff !important; border: none; border-radius: 30px; font-weight: 800;
        letter-spacing: 0.5px; padding: 0.8rem 1.8rem !important; overflow: hidden;
        z-index: 1; transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 4px 15px rgba(56, 189, 248, 0.4), inset 0 1px 0 rgba(255,255,255,0.4);
        display: inline-flex; align-items: center; text-decoration: none;
    }
    .btn-cta-glow:hover { background-position: right center; transform: translateY(-3px) scale(1.02); box-shadow: 0 12px 25px rgba(56, 189, 248, 0.6); }
    </style>
    </head>'''
    if '.btn-cta-glow' not in html:
        html = html.replace('</head>', glow_css)
        
    html = re.sub(
        r'<a href="contact\.html" class="btn btn-primary"[^>]*>.*?Start Project.*?</a>',
        '<a href="contact.html" class="btn btn-primary btn-cta-glow">Start Project <span class="btn-arrow">→</span></a>',
        html,
        flags=re.DOTALL
    )

    with codecs.open('pricing.html', 'w', 'utf-8') as f:
        f.write(html)
    print('pricing.html V6 fixed!')

def fix_cursor():
    with codecs.open('script.js', 'r', 'utf-8') as f:
        js = f.read()
    
    if 'Premium Magnetic Cursor' not in js:
        cursor_logic = '''
/* ─── Premium Magnetic Cursor ─── */
(function(){
    var c=document.createElement('div');
    c.className='cursor';
    c.style.cssText='position:fixed;top:0;left:0;width:20px;height:20px;border:2px solid #38bdf8;border-radius:50%;pointer-events:none;z-index:999999;transform:translate(-50%,-50%);transition:width 0.2s, height 0.2s, background 0.2s, border-color 0.2s;mix-blend-mode:difference;';
    document.body.appendChild(c);
    
    var f=document.createElement('div');
    f.className='cursor-follower';
    f.style.cssText='position:fixed;top:0;left:0;width:8px;height:8px;background:#38bdf8;border-radius:50%;pointer-events:none;z-index:999999;transform:translate(-50%,-50%);';
    document.body.appendChild(f);
    
    var mx=-100,my=-100,cx=-100,cy=-100;
    window.addEventListener('mousemove',function(e){
        mx=e.clientX; my=e.clientY;
        f.style.left=mx+'px'; f.style.top=my+'px';
    });
    
    function loop(){
        cx += (mx - cx) * 0.15;
        cy += (my - cy) * 0.15;
        c.style.left=cx+'px'; c.style.top=cy+'px';
        requestAnimationFrame(loop);
    }
    loop();
    
    function attachCursor(){
        document.querySelectorAll('a, button, .qbtn, input, .wiz-btn, .premium-btn').forEach(function(el){
            if(el.dataset.cursorAttached) return;
            el.dataset.cursorAttached = 'true';
            el.addEventListener('mouseenter',function(){
                c.style.width='50px'; c.style.height='50px'; c.style.background='rgba(56,189,248,0.1)'; c.style.borderColor='rgba(56,189,248,0.5)';
            });
            el.addEventListener('mouseleave',function(){
                c.style.width='20px'; c.style.height='20px'; c.style.background='transparent'; c.style.borderColor='#38bdf8';
            });
        });
    }
    attachCursor();
    // Re-attach occasionally for dynamic elements
    setInterval(attachCursor, 2000);
})();
'''
        js += "\n" + cursor_logic
        with codecs.open('script.js', 'w', 'utf-8') as f:
            f.write(js)
        print("script.js: Global cursor added.")
    
    # Make sure to remove any inline ones from index and services
    for fn in ['index.html', 'services.html']:
        if os.path.exists(fn):
            with codecs.open(fn, 'r', 'utf-8') as f:
                h = f.read()
            h = re.sub(r'/\* ─── Premium Magnetic Cursor ─── \*/.*?\}\)\(\);', '', h, flags=re.DOTALL)
            with codecs.open(fn, 'w', 'utf-8') as f:
                f.write(h)

def cleanup():
    # Remove junk files
    junk = glob.glob('temp_script*.js') + glob.glob('v*_master_fix.py') + glob.glob('patch*.py') + glob.glob('fix_*.py')
    # Keep the current one
    if 'v6_master_fix.py' in junk: junk.remove('v6_master_fix.py')
    
    for j in junk:
        try: os.remove(j)
        except: pass
    print("Cleanup completed. Deleted extra files.")

if __name__ == '__main__':
    fix_index()
    fix_pricing()
    fix_cursor()
    cleanup()
