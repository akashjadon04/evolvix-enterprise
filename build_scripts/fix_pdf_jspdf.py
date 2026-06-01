import re
import os

html_path = 'c:/projects/evolvix/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove html2pdf
html = html.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>', '')
# Add jsPDF
if 'jspdf.umd.min.js' not in html:
    html = html.replace('</head>', '<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>\n</head>')

# Remove the god-pdf-template completely
html = re.sub(r'<!-- GOD MODE PDF TEMPLATE -->.*?<!-- /GOD MODE PDF TEMPLATE -->', '', html, flags=re.DOTALL)

# Find the block where window._buildPlaybookPDF is defined and replace it entirely
new_js = """<script>
window._buildPlaybookPDF = function() {
    if (typeof window.jspdf === 'undefined') {
        alert('PDF Engine loading... please try again in a second.');
        return;
    }
    
    var jsPDF = window.jspdf.jsPDF;
    var doc = new jsPDF({ unit: 'mm', format: 'a4', orientation: 'portrait' });
    
    var data = window.auditData || {};
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
             
    var W = 210, H = 297, ml = 25, mr = 25, cw = W - ml - mr;
    
    // PAGE 1: COVER
    // Dark background
    doc.setFillColor(2, 6, 23); doc.rect(0, 0, W, H, 'F');
    
    // Accents
    doc.setFillColor(14, 116, 144); doc.rect(0, 0, W, 8, 'F');
    doc.setFillColor(56, 189, 248); doc.rect(0, 0, W*0.4, 8, 'F');
    
    doc.setTextColor(255, 255, 255);
    doc.setFontSize(36); doc.setFont('helvetica', 'bold');
    doc.text('Evolvix Technologies', ml, 60);
    
    doc.setTextColor(103, 232, 249);
    doc.setFontSize(12); doc.setFont('courier', 'bold');
    doc.text('// ENTERPRISE STRATEGY AUDIT', ml, 75);
    
    // Confidential tag
    doc.setDrawColor(103, 232, 249); doc.setLineWidth(0.5);
    doc.roundedRect(W - mr - 40, 67, 40, 10, 2, 2, 'D');
    doc.setFontSize(9); doc.text('CONFIDENTIAL', W - mr - 34, 73.5);
    
    // Client Info
    doc.setTextColor(148, 163, 184);
    doc.setFontSize(12); doc.setFont('helvetica', 'normal');
    doc.text('PREPARED EXCLUSIVELY FOR', ml, 160);
    
    doc.setTextColor(255, 255, 255);
    doc.setFontSize(28); doc.setFont('helvetica', 'bold');
    doc.text(name, ml, 172);
    
    doc.setTextColor(203, 213, 225);
    doc.setFontSize(14); doc.setFont('helvetica', 'normal');
    doc.text(btype + '  |  Current MRR: ' + rev, ml, 182);
    
    // Author Info
    doc.setDrawColor(103, 232, 249); doc.setLineWidth(1.5);
    doc.line(ml, 250, ml, 275);
    doc.setTextColor(103, 232, 249);
    doc.setFontSize(10); doc.setFont('courier', 'bold');
    doc.text('AUTHOR', ml + 5, 255);
    
    doc.setTextColor(255, 255, 255);
    doc.setFontSize(18); doc.setFont('helvetica', 'bold');
    doc.text('Akash Jadon', ml + 5, 265);
    
    doc.setTextColor(148, 163, 184);
    doc.setFontSize(12); doc.setFont('helvetica', 'normal');
    doc.text('Founder & Lead Architect', ml + 5, 272);
    
    // PAGE 2: DIAGNOSTICS & PROTOCOL
    doc.addPage();
    
    // Light background
    doc.setFillColor(248, 250, 252); doc.rect(0, 0, W, H, 'F');
    
    // Header
    doc.setTextColor(15, 23, 42);
    doc.setFontSize(24); doc.setFont('helvetica', 'bold');
    doc.text('Diagnostic Analysis', ml, 35);
    doc.setDrawColor(226, 232, 240); doc.setLineWidth(1);
    doc.line(ml, 42, W - mr, 42);
    
    // Score Cards
    var cardW = (cw - 10) / 2;
    doc.setFillColor(255, 255, 255); doc.setDrawColor(203, 213, 225); doc.setLineWidth(0.5);
    doc.roundedRect(ml, 55, cardW, 45, 3, 3, 'FD');
    doc.roundedRect(ml + cardW + 10, 55, cardW, 45, 3, 3, 'FD');
    
    doc.setTextColor(100, 116, 139);
    doc.setFontSize(8); doc.setFont('helvetica', 'bold');
    doc.text('SYSTEM HEALTH SCORE', ml + 8, 65);
    doc.text('PRIMARY BOTTLENECK', ml + cardW + 18, 65);
    
    var sColor = score < 50 ? [239,68,68] : (score < 75 ? [245,158,11] : [16,185,129]);
    var sLabel = score < 50 ? 'CRITICAL STATUS' : (score < 75 ? 'NEEDS OPTIMIZATION' : 'HEALTHY STATUS');
    
    doc.setTextColor.apply(this, sColor);
    doc.setFontSize(36); doc.setFont('helvetica', 'bold');
    doc.text(score + '', ml + 8, 82);
    doc.setTextColor(148, 163, 184); doc.setFontSize(14);
    doc.text('/100', ml + 8 + doc.getTextWidth(score + ''), 82);
    
    doc.setTextColor.apply(this, sColor);
    doc.setFontSize(10);
    doc.text(sLabel, ml + 8, 92);
    
    doc.setTextColor(15, 23, 42);
    doc.setFontSize(16); doc.setFont('helvetica', 'bold');
    var pLines = doc.splitTextToSize(prob, cardW - 16);
    doc.text(pLines, ml + cardW + 18, 80);
    
    // Protocol
    doc.setTextColor(15, 23, 42);
    doc.setFontSize(24); doc.setFont('helvetica', 'bold');
    doc.text('Engineering Protocol', ml, 135);
    doc.setDrawColor(226, 232, 240); doc.setLineWidth(1);
    doc.line(ml, 142, W - mr, 142);
    
    // Solution Box
    doc.setFillColor(224, 242, 254); doc.rect(ml, 155, cw, 35, 'F');
    doc.setDrawColor(14, 165, 233); doc.setLineWidth(2);
    doc.line(ml, 155, ml, 190);
    
    doc.setTextColor(2, 132, 199);
    doc.setFontSize(9); doc.setFont('helvetica', 'bold');
    doc.text('RECOMMENDED SOLUTION', ml + 10, 165);
    
    doc.setTextColor(3, 105, 161);
    doc.setFontSize(16); doc.setFont('helvetica', 'bold');
    doc.text(sol, ml + 10, 175);
    
    doc.setFillColor(255, 255, 255); doc.roundedRect(ml + 10, 180, doc.getTextWidth('Projected Impact: ' + roi) + 6, 6, 1, 1, 'F');
    doc.setTextColor(12, 74, 110); doc.setFontSize(9); doc.setFont('helvetica', 'normal');
    doc.text('Projected Impact: ' + roi, ml + 13, 184.2);
    
    // Deliverables
    doc.setTextColor(100, 116, 139);
    doc.setFontSize(10); doc.setFont('helvetica', 'bold');
    doc.text('WHAT EVOLVIX WILL BUILD:', ml, 210);
    
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
    
    doc.setTextColor(51, 65, 85);
    doc.setFontSize(12); doc.setFont('helvetica', 'normal');
    for(var i=0; i<items.length; i++) {
        doc.setFillColor(224, 242, 254); doc.circle(ml + 3, 220 + (i*9) - 1.5, 2, 'F');
        doc.setTextColor(14, 165, 233); doc.setFontSize(8); doc.setFont('helvetica', 'bold'); doc.text('+', ml + 2.2, 220 + (i*9) - 0.2); 
        doc.setTextColor(51, 65, 85); doc.setFontSize(11); doc.setFont('helvetica', 'normal');
        doc.text(items[i], ml + 10, 220 + (i*9));
    }
    
    // Footer signature
    doc.setDrawColor(203, 213, 225); doc.setLineWidth(0.5);
    doc.line(ml, 270, W - mr, 270);
    
    doc.setTextColor(15, 23, 42);
    doc.setFontSize(12); doc.setFont('helvetica', 'bold');
    doc.text('Akash Jadon', ml, 280);
    doc.setTextColor(100, 116, 139);
    doc.setFontSize(9); doc.setFont('helvetica', 'normal');
    doc.text('evolvixtechnology@gmail.com  |  +91 7668758238', ml, 285);
    
    doc.setTextColor(148, 163, 184);
    doc.setFontSize(9); doc.setFont('helvetica', 'bold');
    doc.text('EVOLVIX.IN', W - mr - doc.getTextWidth('EVOLVIX.IN'), 280);
    
    doc.save('Evolvix_Strategy_Audit_' + name.replace(/[^a-z0-9]/gi, '_').toLowerCase() + '.pdf');
};
</script>"""

html = re.sub(r'<script>\s*window\._buildPlaybookPDF\s*=\s*function.*?</script>', new_js, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
