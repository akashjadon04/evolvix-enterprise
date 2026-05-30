import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add html2pdf and WhatsApp CSS to head
html = html.replace('</head>', '''
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <style>
        .audit-step { transition: opacity 0.3s ease; }
        .wiz-btn { display:block; width:100%; text-align:left; padding:15px; margin-bottom:10px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.1); color:#fff; border-radius:8px; cursor:pointer; font-weight:500; transition:all 0.2s; }
        .wiz-btn:hover { background:rgba(56,189,248,0.1); border-color:#38bdf8; }
        .fab-whatsapp { position:fixed; bottom:30px; right:30px; background:#25D366; color:#fff; width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 15px rgba(37,211,102,0.4); z-index:9999; cursor:pointer; transition:transform 0.3s; text-decoration:none; }
        .fab-whatsapp:hover { transform:scale(1.1); }
        .fab-whatsapp svg { width:32px; height:32px; fill:currentColor; }
        .playbook-modal { display:none; position:fixed; inset:0; background:rgba(0,0,0,0.8); z-index:10000; align-items:center; justify-content:center; }
    </style>
</head>''')

# Replace the Audit Section
new_audit = '''
        <section class="section" id="audit">
            <div class="container">
                <div class="form-card reveal" style="max-width:800px; margin:0 auto; padding:40px; background:rgba(15,23,42,0.8); border:1px solid var(--border-glow); border-radius:16px;">
                    <div style="text-align:center; margin-bottom:30px;">
                        <span style="background:rgba(56,189,248,0.1); color:#38bdf8; padding:5px 15px; border-radius:20px; font-size:0.9rem; font-weight:600;">Astra AI Business Audit</span>
                        <h2 style="color:#fff !important; font-size:2.5rem; margin-top:15px;">Free Enterprise Growth Strategy</h2>
                        <p style="color:var(--text-secondary);">Answer 3 questions and our AI will generate a personalized 2026 scaling roadmap.</p>
                    </div>
                    
                    <div id="audit-wizard">
                        <div class="audit-step" id="step-1">
                            <h3 style="color:#fff; margin-bottom:20px; font-size:1.2rem;">1. What is your primary business type?</h3>
                            <button class="wiz-btn" onclick="nextStep(1, 'btype', 'SaaS / Tech')">SaaS / Technology</button>
                            <button class="wiz-btn" onclick="nextStep(1, 'btype', 'Agency / B2B Services')">Agency / B2B Services</button>
                            <button class="wiz-btn" onclick="nextStep(1, 'btype', 'E-commerce / D2C')">E-commerce / D2C</button>
                            <button class="wiz-btn" onclick="nextStep(1, 'btype', 'Local Business')">Local Business</button>
                        </div>
                        
                        <div class="audit-step" id="step-2" style="display:none;">
                            <h3 style="color:#fff; margin-bottom:20px; font-size:1.2rem;">2. What is your current monthly revenue?</h3>
                            <button class="wiz-btn" onclick="nextStep(2, 'rev', 'Under $10k')">Under $10k (Starting Up)</button>
                            <button class="wiz-btn" onclick="nextStep(2, 'rev', '$10k - $50k')">$10k - $50k (Scaling)</button>
                            <button class="wiz-btn" onclick="nextStep(2, 'rev', '$50k - $100k')">$50k - $100k (Growth)</button>
                            <button class="wiz-btn" onclick="nextStep(2, 'rev', '$100k+')">$100k+ (Enterprise)</button>
                        </div>

                        <div class="audit-step" id="step-3" style="display:none;">
                            <h3 style="color:#fff; margin-bottom:20px; font-size:1.2rem;">3. What is your biggest bottleneck?</h3>
                            <button class="wiz-btn" onclick="nextStep(3, 'neck', 'Not enough Leads')">Not enough high-quality Leads</button>
                            <button class="wiz-btn" onclick="nextStep(3, 'neck', 'Low Conversion Rate')">Low Website Conversion Rate</button>
                            <button class="wiz-btn" onclick="nextStep(3, 'neck', 'Outdated Tech/Website')">Outdated Technology or Design</button>
                            <button class="wiz-btn" onclick="nextStep(3, 'neck', 'Manual Operations')">Too many manual processes</button>
                        </div>

                        <div class="audit-step" id="step-4" style="display:none;">
                            <h3 style="color:#fff; margin-bottom:20px; font-size:1.2rem;">4. Where should we send your AI Report?</h3>
                            <form onsubmit="event.preventDefault(); submitAudit();">
                                <input type="text" id="lead-name" class="input-field" style="margin-bottom:15px;" placeholder="Full Name" required>
                                <input type="email" id="lead-email" class="input-field" style="margin-bottom:15px;" placeholder="Work Email" required>
                                <input type="tel" id="lead-phone" class="input-field" style="margin-bottom:20px;" placeholder="Phone / WhatsApp" required>
                                <button type="submit" id="audit-submit-btn" class="btn btn-primary btn-cta-glow w-full">Generate AI Report</button>
                            </form>
                        </div>
                        
                        <div class="audit-step" id="step-5" style="display:none; text-align:center;">
                            <div id="audit-loading">
                                <div style="border:4px solid #1e293b; border-top:4px solid #38bdf8; border-radius:50%; width:50px; height:50px; animation:spin 1s linear infinite; margin:0 auto 20px;"></div>
                                <h3 style="color:#38bdf8; font-size:1.5rem;">Astra AI is analyzing...</h3>
                                <p style="color:var(--text-secondary);">Generating personalized growth roadmap</p>
                            </div>
                            <div id="audit-success" style="display:none;">
                                <div style="color:#22c55e; font-size:3rem; margin-bottom:10px;">✓</div>
                                <h3 style="color:#fff; font-size:1.5rem; margin-bottom:10px;">Report Generated Successfully</h3>
                                <p style="color:var(--text-secondary); margin-bottom:20px;">A personalized PDF has been generated and sent to your email. We've also initiated an automatic download for your convenience.</p>
                                <button class="btn btn-secondary" onclick="window.open('https://wa.me/917999863831?text=Hi+Akash,+I+just+generated+my+AI+Audit.+Let%27s+talk+strategy!', '_blank')">Discuss Results on WhatsApp</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''
html = re.sub(r'<section class="section" id="audit">.*?</section>', new_audit, html, flags=re.DOTALL)

# Add Playbook Modal (Feature 3)
playbook = '''
    <div class="playbook-modal" id="playbookModal">
        <div class="form-card" style="max-width:500px; position:relative;">
            <button onclick="document.getElementById('playbookModal').style.display='none'" style="position:absolute; top:15px; right:15px; background:none; border:none; color:#fff; cursor:pointer; font-size:1.5rem;">✕</button>
            <h2 style="color:#38bdf8 !important; margin-bottom:10px;">Wait! Before you go...</h2>
            <p style="color:#fff; margin-bottom:20px;">Download our <strong>2026 Enterprise Scaling Playbook</strong>. Learn exactly how companies like Apex Digital and Orbit Systems scaled using our framework.</p>
            <form onsubmit="event.preventDefault(); downloadPlaybook();">
                <input type="email" id="playbook-email" class="input-field" placeholder="Your Best Email" required>
                <button type="submit" class="btn btn-primary w-full" style="margin-top:10px;">Get Free PDF Now</button>
            </form>
        </div>
    </div>
'''
html = html.replace('</body>', playbook + '\\n</body>')

# Add WhatsApp FAB (Feature 5)
fab = '''
    <a href="https://wa.me/917999863831?text=Hi+Akash,+I+want+to+scale+my+business." target="_blank" class="fab-whatsapp" title="Chat with Akash">
        <svg viewBox="0 0 24 24"><path d="M12.012 2c-5.506 0-9.989 4.478-9.99 9.984a9.964 9.964 0 001.333 4.993L2 22l5.233-1.337a9.982 9.982 0 004.778 1.223h.004c5.504 0 9.988-4.478 9.989-9.984 0-2.669-1.037-5.176-2.926-7.062A9.935 9.935 0 0012.012 2zm.004 16.892h-.003a8.315 8.315 0 01-4.247-1.157l-.305-.18-3.155.804.843-3.074-.198-.314A8.293 8.293 0 013.684 11.98c.002-4.582 3.733-8.312 8.324-8.312 2.222.001 4.308.866 5.877 2.437a8.272 8.272 0 012.436 5.882c-.001 4.582-3.731 8.31-8.313 8.31zM16.58 13.9c-.25-.125-1.488-.734-1.718-.818-.23-.084-.399-.125-.567.125-.168.25-.65.818-.797.985-.148.167-.296.188-.546.063-1.32-.656-2.316-1.464-3.21-2.983-.105-.175.101-.163.344-.648.084-.167.042-.313-.021-.438-.063-.125-.567-1.368-.778-1.874-.205-.494-.413-.427-.567-.435l-.485-.008c-.168 0-.441.063-.672.313-.231.25-.882.862-.882 2.102 0 1.24.903 2.438 1.029 2.605.125.167 1.776 2.712 4.302 3.803 1.62.697 2.152.606 2.58.558.468-.053 1.488-.608 1.698-1.196.21-.588.21-1.092.148-1.196-.063-.105-.231-.167-.481-.292z"/></svg>
    </a>
'''
html = html.replace('</body>', fab + '\\n</body>')

# Update Pricing to include coupon (Feature 4)
price_replace = 'Use coupon <strong style="color:var(--c-brand-light);">evolvix 10</strong> for 10% off. Book a strategy call to finalize your project.'
html = html.replace('Custom requirements? Let’s talk.', price_replace)

# Inject JS logic
js_logic = '''
        /* --- AI Audit & Playbook Logic --- */
        let auditData = { name:'', email:'', phone:'', btype:'', rev:'', neck:'' };
        
        function nextStep(current, key, value) {
            auditData[key] = value;
            document.getElementById('step-'+current).style.display = 'none';
            document.getElementById('step-'+(current+1)).style.display = 'block';
        }

        async function submitAudit() {
            auditData.name = document.getElementById('lead-name').value;
            auditData.email = document.getElementById('lead-email').value;
            auditData.phone = document.getElementById('lead-phone').value;
            
            document.getElementById('step-4').style.display = 'none';
            document.getElementById('step-5').style.display = 'block';

            // Send to CRM Backend
            try {
                fetch('https://evolvix-backend-nysg.onrender.com/api/leads', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        name: auditData.name,
                        email: auditData.email,
                        phone: auditData.phone,
                        business_type: auditData.btype,
                        revenue: auditData.rev,
                        bottleneck: auditData.neck
                    })
                });
            } catch(e) {}

            // Generate PDF
            setTimeout(() => {
                document.getElementById('audit-loading').style.display = 'none';
                document.getElementById('audit-success').style.display = 'block';
                
                const element = document.createElement('div');
                element.innerHTML = `
                    <div style="font-family: 'Helvetica', sans-serif; background:#fff; color:#000; padding:60px; width:100%; box-sizing:border-box;">
                        <h1 style="color:#0f172a; border-bottom:2px solid #0f172a; padding-bottom:20px; font-size:32px;">EVOLVIX: 2026 Growth Strategy</h1>
                        <p><strong>Prepared for:</strong> ${auditData.name}</p>
                        <p><strong>Business Type:</strong> ${auditData.btype}</p>
                        <p><strong>Revenue:</strong> ${auditData.rev}</p>
                        <p><strong>Identified Bottleneck:</strong> ${auditData.neck}</p>
                        <h3 style="margin-top:40px;">AI Analysis & Recommendation</h3>
                        <p style="line-height:1.6;">Based on our analysis of your ${auditData.btype} business at the ${auditData.rev} stage, your primary growth blocker is "${auditData.neck}".</p>
                        <p style="line-height:1.6;">To solve this, Evolvix recommends deploying a custom automated pipeline. Book a strategy call with us to see how we can add 30-40% to your bottom line in the next 90 days.</p>
                        <p style="margin-top:40px; color:#64748b;">This document was securely generated by Evolvix AI.</p>
                    </div>
                `;
                html2pdf().from(element).set({ margin:0.5, filename:'Growth_Strategy_Evolvix.pdf', jsPDF:{unit:'in',format:'letter',orientation:'portrait'} }).save();
            }, 3000);
        }

        async function downloadPlaybook() {
            const email = document.getElementById('playbook-email').value;
            // Send to CRM as a playbook lead
            try {
                fetch('https://evolvix-backend-nysg.onrender.com/api/leads', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ name: 'Playbook Download', email: email, phone: 'N/A', business_type: 'N/A', revenue: 'N/A', bottleneck: 'N/A' })
                });
            } catch(e) {}
            
            document.getElementById('playbookModal').style.display = 'none';
            alert('The 2026 Enterprise Scaling Playbook has been sent to your email!');
        }

        // Exit intent detection
        let exitTriggered = false;
        document.addEventListener('mouseleave', e => {
            if (e.clientY < 0 && !exitTriggered) {
                exitTriggered = true;
                document.getElementById('playbookModal').style.display = 'flex';
            }
        });
'''
html = html.replace('</script>', js_logic + '\\n    </script>', 1)

# Modify social proof to use real IP Location
geo_js = '''
        function triggerSocialProof() {
            var bi, tries = 0;
            do { bi = Math.floor(Math.random() * bizNames.length); tries++; } while(usedIdx.indexOf(bi) !== -1 && tries < 20);
            usedIdx.push(bi); if(usedIdx.length > bizNames.length - 2) usedIdx = [];
            var biz = bizNames[bi];
            var action = actions[Math.floor(Math.random() * actions.length)];
            var mins = Math.floor(Math.random() * 8) + 1;
            
            // Fetch real location
            fetch('https://get.geojs.io/v1/ip/geo.json').then(r=>r.json()).then(geo => {
                var city = (geo.city || 'Your Area') + ', ' + (geo.country_code || 'Local');
                if(spTitle) spTitle.textContent = biz + ' ' + action;
                if(spDesc) spDesc.textContent = 'From ' + city + ' · ' + mins + ' min ago';
                if(spToast) spToast.classList.add('show');
                setTimeout(function() { if(spToast) spToast.classList.remove('show'); }, 5000);
            }).catch(e => {
                // fallback
                var city = cities[Math.floor(Math.random() * cities.length)];
                if(spTitle) spTitle.textContent = biz + ' ' + action;
                if(spDesc) spDesc.textContent = 'From ' + city + ' · ' + mins + ' min ago';
                if(spToast) spToast.classList.add('show');
                setTimeout(function() { if(spToast) spToast.classList.remove('show'); }, 5000);
            });
        }
'''
html = re.sub(r'function triggerSocialProof\(\) \{.*?\}', geo_js, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html fully patched with CRM and Lead Gen features.')
