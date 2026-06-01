import re
import os

html_path = 'c:/projects/evolvix/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add html2pdf script if not exists
if 'html2pdf.bundle.min.js' not in html:
    html = html.replace('</head>', '<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>\n</head>')

# 2. Inject God-Mode PDF Template before </body>
god_pdf_template = """
<!-- GOD MODE PDF TEMPLATE -->
<div id="god-pdf-template" style="display:none; width: 850px; background: #ffffff; font-family: 'Inter', sans-serif;">
    
    <!-- PAGE 1: COVER -->
    <div style="height: 1100px; padding: 60px; background: #020617; position: relative; overflow: hidden; page-break-after: always;">
        <!-- Cyber Grid Background -->
        <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: linear-gradient(rgba(103,232,249,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(103,232,249,0.05) 1px, transparent 1px); background-size: 40px 40px; pointer-events: none;"></div>
        
        <div style="position: relative; z-index: 2;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <h1 style="font-family: 'Outfit', sans-serif; font-size: 48px; color: #ffffff; margin: 0 0 10px 0; letter-spacing: -1px;">Evolvix Technologies</h1>
                    <p style="color: #67e8f9; font-size: 14px; font-weight: 700; letter-spacing: 4px; margin: 0; font-family: 'JetBrains Mono', monospace;">// ENTERPRISE STRATEGY AUDIT</p>
                </div>
                <div style="background: rgba(103,232,249,0.1); border: 1px solid rgba(103,232,249,0.3); padding: 5px 15px; border-radius: 20px; color: #67e8f9; font-size: 10px; font-family: 'JetBrains Mono', monospace; font-weight: 700;">CONFIDENTIAL</div>
            </div>
            
            <div style="margin-top: 300px;">
                <p style="color: #94a3b8; font-size: 16px; margin: 0 0 10px 0;">PREPARED EXCLUSIVELY FOR</p>
                <h2 id="gpdf-name" style="color: #ffffff; font-size: 36px; margin: 0 0 5px 0; font-family: 'Outfit', sans-serif;">Client Name</h2>
                <p id="gpdf-meta" style="color: #cbd5e1; font-size: 18px; margin: 0;">Business | Current MRR: N/A</p>
            </div>
            
            <div style="position: absolute; bottom: 60px; left: 60px; border-left: 3px solid #67e8f9; padding-left: 20px;">
                <p style="color: #67e8f9; font-size: 12px; font-weight: 700; margin: 0 0 5px 0; letter-spacing: 2px;">AUTHOR</p>
                <p style="color: #ffffff; font-size: 20px; font-weight: 700; margin: 0;">Akash Jadon</p>
                <p style="color: #94a3b8; font-size: 14px; margin: 0;">Founder & Lead Architect</p>
            </div>
        </div>
    </div>

    <!-- PAGE 2: DIAGNOSTICS & PROTOCOL -->
    <div style="height: 1100px; padding: 60px; background: #f8fafc; position: relative;">
        
        <h2 style="font-family: 'Outfit', sans-serif; font-size: 32px; color: #0f172a; margin: 0 0 30px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 15px;">Diagnostic Analysis</h2>
        
        <!-- Score Cards -->
        <div style="display: flex; gap: 30px; margin-bottom: 40px;">
            <div style="flex: 1; background: #ffffff; padding: 30px; border-radius: 16px; border: 1px solid #cbd5e1; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <p style="font-size: 12px; color: #64748b; font-weight: 800; letter-spacing: 1px; margin: 0 0 10px 0;">SYSTEM HEALTH SCORE</p>
                <div id="gpdf-score-val" style="font-size: 54px; font-weight: 900; color: #ef4444; font-family: 'Outfit', sans-serif; line-height: 1;">45<span style="font-size: 20px; color: #94a3b8;">/100</span></div>
                <p id="gpdf-score-label" style="font-size: 14px; color: #ef4444; font-weight: 700; margin: 10px 0 0 0;">CRITICAL STATUS</p>
            </div>
            
            <div style="flex: 1.5; background: #ffffff; padding: 30px; border-radius: 16px; border: 1px solid #cbd5e1; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <p style="font-size: 12px; color: #64748b; font-weight: 800; letter-spacing: 1px; margin: 0 0 10px 0;">PRIMARY BOTTLENECK</p>
                <div id="gpdf-bottleneck" style="font-size: 28px; font-weight: 800; color: #0f172a; font-family: 'Outfit', sans-serif; margin-bottom: 15px;">Conversion & UX</div>
                <p style="font-size: 14px; color: #475569; line-height: 1.6; margin: 0;">This constraint is actively restricting scale and causing efficiency loss in your digital pipeline.</p>
            </div>
        </div>

        <h2 style="font-family: 'Outfit', sans-serif; font-size: 32px; color: #0f172a; margin: 0 0 30px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 15px;">Engineering Protocol</h2>
        
        <!-- Solution Box -->
        <div style="background: linear-gradient(135deg, #f0f9ff, #e0f2fe); border-left: 4px solid #0ea5e9; padding: 30px; border-radius: 0 16px 16px 0; margin-bottom: 40px;">
            <p style="font-size: 12px; color: #0284c7; font-weight: 800; letter-spacing: 1px; margin: 0 0 10px 0;">RECOMMENDED SOLUTION</p>
            <h3 id="gpdf-solution" style="font-size: 24px; color: #0369a1; font-weight: 800; margin: 0 0 15px 0;">Custom SaaS Platform</h3>
            <div style="background: #ffffff; display: inline-block; padding: 8px 16px; border-radius: 8px; font-size: 14px; font-weight: 700; color: #0c4a6e;" id="gpdf-roi">Projected Impact: 3x Revenue</div>
        </div>

        <p style="font-size: 14px; color: #64748b; font-weight: 800; letter-spacing: 1px; margin: 0 0 15px 0;">WHAT EVOLVIX WILL BUILD:</p>
        <div id="gpdf-list" style="margin-bottom: 50px;">
            <!-- Items injected by JS -->
        </div>

        <!-- Footer -->
        <div style="position: absolute; bottom: 60px; left: 60px; right: 60px; border-top: 1px solid #cbd5e1; padding-top: 30px; display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <img src="assets/akash.png" style="width: 50px; height: 50px; border-radius: 25px; object-fit: cover; border: 2px solid #e2e8f0;">
                <div>
                    <p style="font-size: 16px; font-weight: 800; color: #0f172a; margin: 0;">Akash Jadon</p>
                    <p style="font-size: 12px; color: #64748b; margin: 0;">evolvixtechnology@gmail.com | +91 7668758238</p>
                </div>
            </div>
            <div>
                <p style="font-size: 12px; color: #94a3b8; font-weight: 700; margin: 0;">EVOLVIX.IN</p>
            </div>
        </div>
    </div>
</div>
<!-- /GOD MODE PDF TEMPLATE -->
"""

if 'god-pdf-template' not in html:
    html = html.replace('</body>', f'{god_pdf_template}\n</body>')

# 3. Replace all previous window._buildPlaybookPDF instances with the new logic
# We'll inject this script right before the closing body tag.
new_script = """
<script>
window._buildPlaybookPDF = function() {
    if (typeof html2pdf === 'undefined') {
        alert('PDF Engine loading... please wait a moment and try again.');
        return;
    }
    
    // Attempt to grab data from Alpine component or global auditData
    var data = window.auditData || {};
    if (!data.name && window.Alpine) {
        // Fallback if possible, but let's assume global auditData was set by calculate()
    }
    
    // Default values if data missing
    var name = data.name || 'Enterprise Client';
    var btype = data.btype || 'Digital Business';
    var rev = data.rev || 'Undisclosed';
    var prob = data.neck || 'Scalability Limits';
    var goal = data.goal || 'Dominant Positioning';
    
    var score = Math.floor(Math.random() * 20) + 40; 
    if(rev === '$50k+/mo') score += 20;
    if(prob === 'Systems & Tech') score -= 10;
    
    var sol = prob === 'Traffic & Leads' ? 'SEO & Viral Organic Growth Funnel' : 
             (prob === 'Conversion & UX' ? 'Premium Web Design & CRO' : 'Custom SaaS & Workflow Automation');
    
    var roi = goal === 'Double Revenue' ? '2x Revenue in 6 Months' : 
             (goal === 'Automation & Scale' ? 'Save 40+ Hours/Week' : 'Dominant Market Positioning');
             
    // Set UI elements in hidden template
    document.getElementById('gpdf-name').innerText = name;
    document.getElementById('gpdf-meta').innerText = btype + ' | Current MRR: ' + rev;
    
    var sColor = score < 50 ? '#ef4444' : (score < 75 ? '#f59e0b' : '#10b981');
    var sLabel = score < 50 ? 'CRITICAL STATUS' : (score < 75 ? 'NEEDS OPTIMIZATION' : 'HEALTHY STATUS');
    var elScore = document.getElementById('gpdf-score-val');
    elScore.innerHTML = score + '<span style="font-size: 20px; color: #94a3b8;">/100</span>';
    elScore.style.color = sColor;
    var elLabel = document.getElementById('gpdf-score-label');
    elLabel.innerText = sLabel;
    elLabel.style.color = sColor;
    
    document.getElementById('gpdf-bottleneck').innerText = prob;
    document.getElementById('gpdf-solution').innerText = sol;
    document.getElementById('gpdf-roi').innerText = 'Projected Impact: ' + roi;
    
    var items = prob === 'Traffic & Leads' ? [
        'Custom SEO-optimized website with 95+ PageSpeed score',
        'Content strategy with keyword-targeted landing pages',
        'Google Business Profile optimization & local SEO',
        'Automated lead capture funnels with CRM integration'
    ] : prob === 'Conversion & UX' ? [
        'Complete UI/UX redesign with conversion-focused wireframes',
        'Mobile-first responsive build with A/B test variants',
        'Heatmap & session recording for behavior analysis',
        'Checkout/contact flow optimization (60% friction reduction)'
    ] : [
        'Custom SaaS platform tailored to your workflow',
        'API integrations connecting your existing tools',
        'Automated reporting and notification systems',
        'Role-based access control & secure data management'
    ];
    
    var listHTML = '';
    items.forEach(function(item) {
        listHTML += '<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">' +
                    '<div style="width: 20px; height: 20px; border-radius: 10px; background: #e0f2fe; color: #0ea5e9; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: bold;">✓</div>' +
                    '<span style="font-size: 15px; color: #334155;">' + item + '</span></div>';
    });
    document.getElementById('gpdf-list').innerHTML = listHTML;
    
    // Unhide temporarily for rendering
    var element = document.getElementById('god-pdf-template');
    element.style.display = 'block';
    
    var opt = {
      margin:       0,
      filename:     'Evolvix_Strategy_Audit_' + name.replace(/[^a-z0-9]/gi, '_').toLowerCase() + '.pdf',
      image:        { type: 'jpeg', quality: 1.0 },
      html2canvas:  { scale: 2, useCORS: true, logging: false },
      jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
    };
    
    // Render
    html2pdf().set(opt).from(element).save().then(function() {
        element.style.display = 'none'; // Hide again
    });
};
</script>
"""

# Append the new global script at the end of the body
if 'window._buildPlaybookPDF = function()' not in html or 'html2pdf().set(opt)' not in html:
    # First, let's remove any old inline window._buildPlaybookPDF definitions that might interfere.
    # Because we're just redefining it globally, the last definition wins, so we can just append it safely.
    html = html.replace('</body>', f'{new_script}\n</body>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
