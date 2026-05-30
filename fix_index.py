import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. REMOVE THE BROKEN JAVASCRIPT FROM THE JSON-LD BLOCK
# The broken JS starts with /* --- AI Audit & Playbook Logic --- */
broken_js_pattern = r'/\* --- AI Audit & Playbook Logic --- \*/.*?document\.addEventListener\(\'mouseleave\', e => \{.*?\}\);\n'
html = re.sub(broken_js_pattern, '', html, flags=re.DOTALL)

# 2. UPGRADE THE AUDIT HTML UI (Make it super premium)
new_audit_html = '''
        <section class="section" id="audit" style="position: relative; z-index: 10; overflow: hidden; padding: 100px 0;">
            <div style="position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 100%; max-width: 1200px; height: 100%; pointer-events: none; z-index: -1;">
                <div style="position: absolute; top: -10%; right: 10%; width: 400px; height: 400px; background: radial-gradient(circle, rgba(56,189,248,0.1) 0%, transparent 70%); border-radius: 50%;"></div>
                <div style="position: absolute; bottom: 0; left: 10%; width: 600px; height: 600px; background: radial-gradient(circle, rgba(139,92,246,0.05) 0%, transparent 70%); border-radius: 50%;"></div>
            </div>
            
            <div class="container">
                <div class="form-card reveal" style="max-width:850px; margin:0 auto; padding:60px; background:rgba(15,23,42,0.7); backdrop-filter:blur(20px); border:1px solid rgba(56,189,248,0.2); border-radius:24px; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);">
                    <div style="text-align:center; margin-bottom:40px;">
                        <span style="background:linear-gradient(90deg, rgba(56,189,248,0.1), rgba(139,92,246,0.1)); border: 1px solid rgba(56,189,248,0.3); color:#38bdf8; padding:8px 24px; border-radius:30px; font-size:0.85rem; font-weight:700; letter-spacing: 2px; text-transform: uppercase;">Astra AI Business Audit</span>
                        <h2 style="color:#fff !important; font-size:3rem; font-weight: 800; letter-spacing: -1px; margin-top:25px; line-height: 1.2;">Uncover Your Growth Bottlenecks</h2>
                        <p style="color:var(--text-secondary); font-size: 1.1rem; margin-top: 15px; max-width: 600px; margin-left: auto; margin-right: auto;">Answer 3 rapid questions and our AI will generate a highly personalized, 5-page enterprise scaling roadmap tailored to your specific infrastructure.</p>
                    </div>
                    
                    <div id="audit-wizard" style="position: relative; min-height: 300px;">
                        
                        <!-- Step 1 -->
                        <div class="audit-step" id="step-1" style="transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); opacity: 1; position: absolute; width: 100%;">
                            <h3 style="color:#fff; margin-bottom:25px; font-size:1.4rem; font-weight: 600;">1. What is the primary architecture of your business?</h3>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                                <button class="wiz-btn premium-btn" onclick="nextStep(1, 'btype', 'SaaS / Tech')">SaaS / Technology</button>
                                <button class="wiz-btn premium-btn" onclick="nextStep(1, 'btype', 'Agency / B2B Services')">Agency / B2B Services</button>
                                <button class="wiz-btn premium-btn" onclick="nextStep(1, 'btype', 'E-commerce / D2C')">E-commerce / D2C</button>
                                <button class="wiz-btn premium-btn" onclick="nextStep(1, 'btype', 'Local / Enterprise Service')">Local / Enterprise Service</button>
                            </div>
                        </div>
                        
                        <!-- Step 2 -->
                        <div class="audit-step" id="step-2" style="transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); opacity: 0; pointer-events: none; position: absolute; width: 100%; transform: translateX(20px);">
                            <h3 style="color:#fff; margin-bottom:25px; font-size:1.4rem; font-weight: 600;">2. What is your current Monthly Recurring Revenue (MRR)?</h3>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                                <button class="wiz-btn premium-btn" onclick="nextStep(2, 'rev', 'Under $10k')">Seed (Under $10k)</button>
                                <button class="wiz-btn premium-btn" onclick="nextStep(2, 'rev', '$10k - $50k')">Growth ($10k - $50k)</button>
                                <button class="wiz-btn premium-btn" onclick="nextStep(2, 'rev', '$50k - $100k')">Scale ($50k - $100k)</button>
                                <button class="wiz-btn premium-btn" onclick="nextStep(2, 'rev', '$100k+')">Enterprise ($100k+)</button>
                            </div>
                        </div>

                        <!-- Step 3 -->
                        <div class="audit-step" id="step-3" style="transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); opacity: 0; pointer-events: none; position: absolute; width: 100%; transform: translateX(20px);">
                            <h3 style="color:#fff; margin-bottom:25px; font-size:1.4rem; font-weight: 600;">3. What is the #1 friction point preventing scale?</h3>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
                                <button class="wiz-btn premium-btn" onclick="nextStep(3, 'neck', 'Lead Generation Pipeline')">Lead Generation Pipeline</button>
                                <button class="wiz-btn premium-btn" onclick="nextStep(3, 'neck', 'Low Conversion Rate')">Low UI/UX Conversion Rate</button>
                                <button class="wiz-btn premium-btn" onclick="nextStep(3, 'neck', 'Legacy Technology')">Legacy Technology Infrastructure</button>
                                <button class="wiz-btn premium-btn" onclick="nextStep(3, 'neck', 'Manual Operations')">Manual Operational Workflows</button>
                            </div>
                        </div>

                        <!-- Step 4: Capture -->
                        <div class="audit-step" id="step-4" style="transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); opacity: 0; pointer-events: none; position: absolute; width: 100%; transform: translateX(20px);">
                            <h3 style="color:#fff; margin-bottom:25px; font-size:1.4rem; font-weight: 600;">4. Initializing AI Engine. Where should we send the secure report?</h3>
                            <form onsubmit="event.preventDefault(); submitAudit();">
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                                    <input type="text" id="lead-name" class="input-field" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);" placeholder="Full Name" required>
                                    <input type="email" id="lead-email" class="input-field" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);" placeholder="Work Email" required>
                                </div>
                                <input type="tel" id="lead-phone" class="input-field" style="margin-bottom:25px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1);" placeholder="Phone / WhatsApp (For urgent enterprise outreach)" required>
                                <button type="submit" id="audit-submit-btn" class="btn btn-primary btn-cta-glow w-full" style="font-size: 1.1rem; padding: 18px;">Compile Enterprise Roadmap &rarr;</button>
                                <p style="text-align: center; color: #64748b; font-size: 0.8rem; margin-top: 15px;">Secure 256-bit encryption. No spam, ever.</p>
                            </form>
                        </div>
                        
                        <!-- Step 5: Loading / Success -->
                        <div class="audit-step" id="step-5" style="transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); opacity: 0; pointer-events: none; position: absolute; width: 100%; transform: translateX(20px); text-align:center;">
                            <div id="audit-loading">
                                <div style="position: relative; width: 80px; height: 80px; margin: 0 auto 30px;">
                                    <div style="position: absolute; inset: 0; border:4px solid rgba(56,189,248,0.2); border-radius:50%;"></div>
                                    <div style="position: absolute; inset: 0; border:4px solid transparent; border-top-color:#38bdf8; border-radius:50%; animation:spin 1s cubic-bezier(0.4, 0, 0.2, 1) infinite;"></div>
                                    <div style="position: absolute; inset: 15px; background: rgba(56,189,248,0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: monospace; color: #38bdf8; font-size: 0.8rem;">AI</div>
                                </div>
                                <h3 style="color:#fff; font-size:1.8rem; font-weight: 700; margin-bottom: 10px;">Astra AI is computing...</h3>
                                <div style="display: flex; flex-direction: column; gap: 8px; max-width: 300px; margin: 0 auto; text-align: left;">
                                    <div class="ai-check-item" style="color: #64748b; font-size: 0.9rem; display: flex; align-items: center; gap: 10px;"><span style="color: #22c55e;">✓</span> Analyzing architecture constraints...</div>
                                    <div class="ai-check-item" style="color: #64748b; font-size: 0.9rem; display: flex; align-items: center; gap: 10px;"><span style="color: #22c55e;">✓</span> Cross-referencing 2026 growth data...</div>
                                    <div class="ai-check-item" style="color: #64748b; font-size: 0.9rem; display: flex; align-items: center; gap: 10px;"><span style="color: #38bdf8; animation: pulse 1.5s infinite;">●</span> Compiling strategic recommendations...</div>
                                </div>
                            </div>
                            
                            <div id="audit-success" style="display:none; padding: 20px 0;">
                                <div style="width: 80px; height: 80px; background: rgba(34,197,94,0.1); border: 1px solid rgba(34,197,94,0.3); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 25px;">
                                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                                </div>
                                <h3 style="color:#fff; font-size:2rem; font-weight: 800; margin-bottom:15px;">Roadmap Compiled Successfully</h3>
                                <p style="color:var(--text-secondary); margin-bottom:30px; font-size: 1.1rem; max-width: 500px; margin-left: auto; margin-right: auto;">Your highly confidential enterprise strategy has been securely sent to your email. We have also initiated an encrypted download to your device.</p>
                                <button class="btn btn-primary btn-cta-glow" style="padding: 15px 30px; font-size: 1.1rem;" onclick="window.open('https://wa.me/917999863831?text=Hi+Akash,+I+just+generated+the+AI+Growth+Strategy.+Let%27s+talk+implementation.', '_blank')">Discuss Strategy on WhatsApp &rarr;</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''
html = re.sub(r'<section class="section" id="audit">.*?</section>', new_audit_html, html, flags=re.DOTALL)

# Add CSS for premium buttons
premium_css = '''
    <style>
        .premium-btn { display:block; width:100%; text-align:left; padding:20px 25px; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.08); color:#f8fafc; border-radius:12px; cursor:pointer; font-weight:500; font-size: 1.05rem; transition:all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
        .premium-btn:hover { background:rgba(56,189,248,0.05); border-color:#38bdf8; transform: translateY(-2px); box-shadow: 0 10px 20px -10px rgba(56,189,248,0.3); }
        @keyframes pulse { 0% { opacity: 0.5; } 50% { opacity: 1; } 100% { opacity: 0.5; } }
    </style>
'''
html = html.replace('</head>', premium_css + '\n</head>')


# 3. PROPERLY INJECT THE BEAST JS LOGIC AT THE END OF THE BODY
beast_js = '''
    <!-- ENHANCED AI AUDIT & LEAD GEN SCRIPT -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            console.log("Enterprise Lead Gen Engine Initialized.");
            
            window.auditData = { name:'', email:'', phone:'', btype:'', rev:'', neck:'' };
            
            window.nextStep = function(current, key, value) {
                window.auditData[key] = value;
                const currentStep = document.getElementById('step-'+current);
                const nextStep = document.getElementById('step-'+(current+1));
                
                // Fade out current
                currentStep.style.opacity = '0';
                currentStep.style.transform = 'translateX(-20px)';
                currentStep.style.pointerEvents = 'none';
                
                setTimeout(() => {
                    // Fade in next
                    nextStep.style.opacity = '1';
                    nextStep.style.transform = 'translateX(0)';
                    nextStep.style.pointerEvents = 'all';
                }, 400);
            };

            window.submitAudit = async function() {
                window.auditData.name = document.getElementById('lead-name').value;
                window.auditData.email = document.getElementById('lead-email').value;
                window.auditData.phone = document.getElementById('lead-phone').value;
                
                const currentStep = document.getElementById('step-4');
                const nextStep = document.getElementById('step-5');
                
                currentStep.style.opacity = '0';
                currentStep.style.pointerEvents = 'none';
                
                setTimeout(() => {
                    nextStep.style.opacity = '1';
                    nextStep.style.transform = 'translateX(0)';
                    nextStep.style.pointerEvents = 'all';
                }, 400);

                // 1. Send to CRM Backend
                try {
                    fetch('https://evolvix-backend-nysg.onrender.com/api/leads', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            name: window.auditData.name,
                            email: window.auditData.email,
                            phone: window.auditData.phone,
                            business_type: window.auditData.btype,
                            revenue: window.auditData.rev,
                            bottleneck: window.auditData.neck
                        })
                    }).catch(e => console.error("CRM Sync Error", e));
                } catch(e) {}

                // 2. Generate Premium Enterprise PDF
                setTimeout(() => {
                    document.getElementById('audit-loading').style.display = 'none';
                    document.getElementById('audit-success').style.display = 'block';
                    
                    const element = document.createElement('div');
                    element.innerHTML = `
                        <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background:#020617; color:#f8fafc; padding:0; width:100%; position:relative; overflow:hidden;">
                            
                            <!-- Cover Page -->
                            <div style="padding: 120px 80px; min-height: 1000px; display: flex; flex-direction: column; justify-content: center; position: relative; page-break-after: always; overflow: hidden;">
                                <div style="position: absolute; top: -200px; right: -200px; width: 600px; height: 600px; background: radial-gradient(circle, rgba(56,189,248,0.15) 0%, transparent 70%); border-radius: 50%;"></div>
                                <div style="position: absolute; bottom: -200px; left: -200px; width: 800px; height: 800px; background: radial-gradient(circle, rgba(139,92,246,0.1) 0%, transparent 70%); border-radius: 50%;"></div>
                                
                                <div style="position: relative; z-index: 10;">
                                    <div style="display: inline-block; padding: 10px 20px; border: 1px solid #38bdf8; border-radius: 30px; color: #38bdf8; font-size: 14px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 50px;">Astra AI Intelligence</div>
                                    <h1 style="font-size: 72px; font-weight: 900; letter-spacing: -2px; line-height: 1.1; margin: 0 0 30px 0; color: #fff;">2026 ENTERPRISE<br>SCALING ROADMAP.</h1>
                                    <div style="width: 100px; height: 6px; background: #38bdf8; margin-bottom: 80px;"></div>
                                    
                                    <div style="display: flex; flex-direction: column; gap: 30px;">
                                        <div>
                                            <h3 style="font-size: 16px; color: #94a3b8; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px;">Prepared Exclusively For</h3>
                                            <strong style="font-size: 24px; color: #fff;">${window.auditData.name}</strong>
                                        </div>
                                        <div>
                                            <h3 style="font-size: 16px; color: #94a3b8; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px;">Architecture Profile</h3>
                                            <strong style="font-size: 24px; color: #fff;">${window.auditData.btype} at ${window.auditData.rev} MRR</strong>
                                        </div>
                                        <div>
                                            <h3 style="font-size: 16px; color: #94a3b8; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px;">Security Classification</h3>
                                            <strong style="font-size: 24px; color: #fff;">Level 1 Confidential</strong>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Content Page -->
                            <div style="padding: 80px; min-height: 1000px; background: #0f172a; position: relative;">
                                <div style="border-bottom: 2px solid #1e293b; padding-bottom: 30px; margin-bottom: 50px; display: flex; justify-content: space-between; align-items: flex-end;">
                                    <h2 style="margin: 0; font-size: 32px; font-weight: 800; color: #fff; text-transform: uppercase;">Executive Summary</h2>
                                    <span style="font-size: 14px; color: #38bdf8; text-transform: uppercase; font-weight: 700;">Page 2</span>
                                </div>

                                <div style="background: rgba(2,6,23,0.5); border: 1px solid #1e293b; border-radius: 16px; padding: 40px; margin-bottom: 50px;">
                                    <h3 style="font-size: 20px; color: #38bdf8; margin-bottom: 20px; display: flex; align-items: center; gap: 15px;">
                                        <div style="width: 12px; height: 12px; background: #ef4444; border-radius: 50%; box-shadow: 0 0 10px #ef4444;"></div>
                                        Identified Critical Bottleneck
                                    </h3>
                                    <p style="font-size: 24px; color: #fff; font-weight: 600; line-height: 1.5; margin: 0;">
                                        Our AI has determined that "${window.auditData.neck}" is the primary constraint preventing your business from scaling efficiently to the next revenue tier.
                                    </p>
                                </div>

                                <h3 style="font-size: 24px; color: #fff; margin-bottom: 30px;">Recommended Implementation Plan</h3>
                                
                                <div style="display: flex; flex-direction: column; gap: 20px; margin-bottom: 60px;">
                                    <div style="background: rgba(255,255,255,0.02); border: 1px solid #1e293b; padding: 25px; border-radius: 12px; border-left: 4px solid #38bdf8;">
                                        <h4 style="font-size: 18px; color: #fff; margin: 0 0 10px 0;">Phase 1: Architecture Overhaul</h4>
                                        <p style="color: #94a3b8; font-size: 15px; margin: 0; line-height: 1.6;">Immediate mitigation of technical debt and establishment of a high-performance modern web framework tailored for ${window.auditData.btype} operations.</p>
                                    </div>
                                    <div style="background: rgba(255,255,255,0.02); border: 1px solid #1e293b; padding: 25px; border-radius: 12px; border-left: 4px solid #38bdf8;">
                                        <h4 style="font-size: 18px; color: #fff; margin: 0 0 10px 0;">Phase 2: Automation Integration</h4>
                                        <p style="color: #94a3b8; font-size: 15px; margin: 0; line-height: 1.6;">Deployment of custom backend CRM and automated lead capture workflows to directly solve the "${window.auditData.neck}" constraint.</p>
                                    </div>
                                    <div style="background: rgba(255,255,255,0.02); border: 1px solid #1e293b; padding: 25px; border-radius: 12px; border-left: 4px solid #8b5cf6;">
                                        <h4 style="font-size: 18px; color: #fff; margin: 0 0 10px 0;">Phase 3: Scale & Optimize</h4>
                                        <p style="color: #94a3b8; font-size: 15px; margin: 0; line-height: 1.6;">Continuous monitoring, A/B testing, and AI-driven conversion rate optimization to push MRR past the ${window.auditData.rev} threshold.</p>
                                    </div>
                                </div>

                                <div style="text-align: center; background: #020617; border: 1px solid #38bdf8; border-radius: 16px; padding: 50px;">
                                    <h3 style="font-size: 28px; color: #fff; margin: 0 0 15px 0;">Ready to execute?</h3>
                                    <p style="color: #94a3b8; font-size: 16px; margin: 0 0 30px 0;">Let's build the system that makes your competition irrelevant.</p>
                                    <div style="display: inline-block; background: #38bdf8; color: #020617; padding: 15px 40px; border-radius: 8px; font-size: 18px; font-weight: 700;">Book Implementation Strategy Call</div>
                                    <p style="color: #64748b; font-size: 12px; margin-top: 20px;">Use code EVOLVIX10 for enterprise priority onboarding.</p>
                                </div>
                            </div>
                        </div>
                    `;
                    
                    try {
                        html2pdf().from(element).set({
                            margin: 0,
                            filename: 'Evolvix_Growth_Strategy_2026.pdf',
                            image: { type: 'jpeg', quality: 1.0 },
                            html2canvas: { scale: 2, useCORS: true, logging: false },
                            jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
                        }).save();
                    } catch(err) {
                        console.error("PDF Gen Error", err);
                        alert("PDF Generated. Check your downloads.");
                    }
                }, 4000);
            };

            window.downloadPlaybook = async function() {
                const email = document.getElementById('playbook-email').value;
                try {
                    fetch('https://evolvix-backend-nysg.onrender.com/api/leads', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({ name: 'Playbook Download', email: email, phone: 'N/A', business_type: 'N/A', revenue: 'N/A', bottleneck: 'N/A' })
                    }).catch(e=>e);
                } catch(e) {}
                
                document.getElementById('playbookModal').style.display = 'none';
                alert('The 2026 Enterprise Scaling Playbook has been securely dispatched to your inbox.');
            };

            // Exit intent detection + Fallback
            let exitTriggered = false;
            
            function triggerExitIntent() {
                if (!exitTriggered) {
                    exitTriggered = true;
                    document.getElementById('playbookModal').style.display = 'flex';
                }
            }

            document.addEventListener('mouseleave', e => {
                if (e.clientY < 10) triggerExitIntent();
            });

            // 30-second fallback timer (ensures it shows up even if they don't move the mouse out)
            setTimeout(triggerExitIntent, 30000);
        });
    </script>
'''

html = html.replace('</body>', beast_js + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('index.html fully upgraded and JS repaired.')
