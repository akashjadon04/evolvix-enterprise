import os

privacy_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy - Evolvix Enterprise</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #020617;
            --bg-surface: #0f172a;
            --border-glow: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent: #38bdf8;
            --accent-glow: 0 0 20px rgba(56, 189, 248, 0.4);
        }
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
        body { background: var(--bg-base); color: var(--text-primary); line-height: 1.8; overflow-x: hidden; }
        
        /* Hero Section */
        .legal-hero { padding: 120px 20px 80px; text-align: center; position: relative; border-bottom: 1px solid var(--border-glow); }
        .legal-hero::before { content: ''; position: absolute; top: -200px; left: 50%; transform: translateX(-50%); width: 800px; height: 800px; background: radial-gradient(circle, rgba(56,189,248,0.1) 0%, transparent 70%); border-radius: 50%; z-index: -1; pointer-events: none; }
        .badge { display: inline-block; padding: 8px 24px; border-radius: 30px; background: rgba(56,189,248,0.1); border: 1px solid rgba(56,189,248,0.3); color: var(--accent); font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px; }
        .legal-hero h1 { font-family: 'Outfit', sans-serif; font-size: 4rem; font-weight: 900; letter-spacing: -2px; margin-bottom: 20px; color: #fff; }
        .legal-hero p { font-size: 1.2rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto; }
        
        /* Layout */
        .legal-container { max-width: 1200px; margin: 0 auto; padding: 60px 20px; display: grid; grid-template-columns: 300px 1fr; gap: 60px; }
        @media (max-width: 900px) { .legal-container { grid-template-columns: 1fr; } }
        
        /* Sidebar */
        .sidebar { position: sticky; top: 40px; }
        .sidebar ul { list-style: none; border-left: 2px solid var(--border-glow); padding-left: 20px; }
        .sidebar li { margin-bottom: 15px; }
        .sidebar a { color: var(--text-secondary); text-decoration: none; font-size: 0.95rem; font-weight: 500; transition: color 0.3s; }
        .sidebar a:hover, .sidebar a.active { color: var(--accent); }
        
        /* Content */
        .content-panel { background: rgba(15,23,42,0.4); backdrop-filter: blur(20px); border: 1px solid var(--border-glow); border-radius: 24px; padding: 60px; }
        .content-panel h2 { font-family: 'Outfit', sans-serif; font-size: 2rem; color: #fff; margin-top: 50px; margin-bottom: 20px; border-bottom: 1px solid var(--border-glow); padding-bottom: 15px; }
        .content-panel h2:first-child { margin-top: 0; }
        .content-panel p { color: var(--text-secondary); margin-bottom: 20px; font-size: 1.05rem; }
        .content-panel ul { margin-left: 20px; margin-bottom: 20px; color: var(--text-secondary); }
        .content-panel li { margin-bottom: 10px; }
        .highlight-box { background: rgba(56,189,248,0.05); border-left: 4px solid var(--accent); padding: 20px; border-radius: 0 12px 12px 0; margin: 30px 0; }
        
        .nav-link { position: absolute; top: 40px; left: 40px; color: var(--text-secondary); text-decoration: none; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; font-weight: 600; display: flex; align-items: center; gap: 10px; transition: color 0.3s; }
        .nav-link:hover { color: #fff; }
    </style>
</head>
<body>
    <a href="index.html" class="nav-link"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg> Return Home</a>
    
    <div class="legal-hero">
        <span class="badge">Legal Documentation</span>
        <h1>Privacy Policy</h1>
        <p>Enterprise-grade security and transparency for your data. Last updated: January 2026.</p>
    </div>
    
    <div class="legal-container">
        <aside class="sidebar">
            <h3 style="color: #fff; margin-bottom: 20px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px;">Contents</h3>
            <ul>
                <li><a href="#collection">1. Data Collection</a></li>
                <li><a href="#usage">2. Data Utilization</a></li>
                <li><a href="#sharing">3. Enterprise Data Sharing</a></li>
                <li><a href="#security">4. Advanced Security Protocols</a></li>
                <li><a href="#rights">5. Your Legal Rights</a></li>
                <li><a href="#contact">6. Contact Data Protection</a></li>
            </ul>
        </aside>
        
        <main class="content-panel">
            <div class="highlight-box">
                <p style="margin:0; color: #fff; font-weight: 600;">Evolvix Technologies ("we", "us", or "our") is committed to absolute data sovereignty. We process your data exclusively to deliver high-performance enterprise software.</p>
            </div>

            <h2 id="collection">1. Enterprise Data Collection</h2>
            <p>In the course of delivering enterprise software development services, we collect strictly necessary data sets. This includes:</p>
            <ul>
                <li><strong>Identity Data:</strong> First name, last name, corporate username, and cryptographic authentication tokens.</li>
                <li><strong>Contact Data:</strong> Corporate email address, billing address, and emergency engineering contact numbers.</li>
                <li><strong>Technical Data:</strong> IP address, browser architecture, timezone settings, geolocation via API, and operating system identifiers utilized to interact with our Client Portal.</li>
                <li><strong>Usage Data:</strong> Analytical telemetry regarding how you utilize our AI Audit, software interfaces, and documentation.</li>
            </ul>

            <h2 id="usage">2. Data Utilization & Machine Learning</h2>
            <p>Your data is the backbone of our personalized enterprise delivery. We utilize it under the following legal frameworks:</p>
            <ul>
                <li>To compile dynamic, highly-personalized AI Growth Roadmaps using the Astra AI Engine.</li>
                <li>To securely process financial transactions, invoices, and wire transfer logging.</li>
                <li>To manage our contractual relationship with you, including notifying you about architectural updates.</li>
            </ul>

            <h2 id="sharing">3. Zero-Trust Data Sharing</h2>
            <p>We operate on a zero-trust architecture. We do <strong>not</strong> sell, rent, or blindly transfer your enterprise architecture details to third parties. Data is only shared with:</p>
            <ul>
                <li><strong>Infrastructure Providers:</strong> Encrypted databases hosted on AWS/Render.</li>
                <li><strong>Legal Compliance:</strong> When strictly mandated by international law enforcement accompanied by a verified warrant.</li>
            </ul>

            <h2 id="security">4. Advanced Security Protocols</h2>
            <p>Our Client Portal and backend infrastructure utilize AES-256 military-grade encryption for data at rest, and TLS 1.3 for data in transit. While no system is theoretically impenetrable, our enterprise safeguards are designed to mitigate 99.9% of modern cyber threats.</p>

            <h2 id="rights">5. Your Legal Rights (GDPR & CCPA Compliant)</h2>
            <p>Depending on your jurisdiction, you possess the right to:</p>
            <ul>
                <li>Request absolute deletion of your enterprise records ("Right to be Forgotten").</li>
                <li>Request a cryptographic export of your CRM data.</li>
                <li>Opt-out of automated AI profiling and marketing communications.</li>
            </ul>

            <h2 id="contact">6. Contact Data Protection</h2>
            <p>For any legal inquiries, data deletion requests, or compliance audits, please contact our Lead Architect and Data Protection Officer directly:</p>
            <p><strong>Akash Jadon</strong><br>Email: contact@evolvix.tech<br>WhatsApp: +91 7668758238</p>
        </main>
    </div>
</body>
</html>'''

terms_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Service - Evolvix Enterprise</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #020617;
            --bg-surface: #0f172a;
            --border-glow: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent: #38bdf8;
            --accent-glow: 0 0 20px rgba(56, 189, 248, 0.4);
        }
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
        body { background: var(--bg-base); color: var(--text-primary); line-height: 1.8; overflow-x: hidden; }
        
        .legal-hero { padding: 120px 20px 80px; text-align: center; position: relative; border-bottom: 1px solid var(--border-glow); }
        .legal-hero::before { content: ''; position: absolute; top: -200px; left: 50%; transform: translateX(-50%); width: 800px; height: 800px; background: radial-gradient(circle, rgba(139,92,246,0.1) 0%, transparent 70%); border-radius: 50%; z-index: -1; pointer-events: none; }
        .badge { display: inline-block; padding: 8px 24px; border-radius: 30px; background: rgba(139,92,246,0.1); border: 1px solid rgba(139,92,246,0.3); color: #c084fc; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 30px; }
        .legal-hero h1 { font-family: 'Outfit', sans-serif; font-size: 4rem; font-weight: 900; letter-spacing: -2px; margin-bottom: 20px; color: #fff; }
        .legal-hero p { font-size: 1.2rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto; }
        
        .legal-container { max-width: 1200px; margin: 0 auto; padding: 60px 20px; display: grid; grid-template-columns: 300px 1fr; gap: 60px; }
        @media (max-width: 900px) { .legal-container { grid-template-columns: 1fr; } }
        
        .sidebar { position: sticky; top: 40px; }
        .sidebar ul { list-style: none; border-left: 2px solid var(--border-glow); padding-left: 20px; }
        .sidebar li { margin-bottom: 15px; }
        .sidebar a { color: var(--text-secondary); text-decoration: none; font-size: 0.95rem; font-weight: 500; transition: color 0.3s; }
        .sidebar a:hover, .sidebar a.active { color: #c084fc; }
        
        .content-panel { background: rgba(15,23,42,0.4); backdrop-filter: blur(20px); border: 1px solid var(--border-glow); border-radius: 24px; padding: 60px; }
        .content-panel h2 { font-family: 'Outfit', sans-serif; font-size: 2rem; color: #fff; margin-top: 50px; margin-bottom: 20px; border-bottom: 1px solid var(--border-glow); padding-bottom: 15px; }
        .content-panel h2:first-child { margin-top: 0; }
        .content-panel p { color: var(--text-secondary); margin-bottom: 20px; font-size: 1.05rem; }
        .content-panel ul { margin-left: 20px; margin-bottom: 20px; color: var(--text-secondary); }
        .content-panel li { margin-bottom: 10px; }
        .highlight-box { background: rgba(139,92,246,0.05); border-left: 4px solid #c084fc; padding: 20px; border-radius: 0 12px 12px 0; margin: 30px 0; }
        
        .nav-link { position: absolute; top: 40px; left: 40px; color: var(--text-secondary); text-decoration: none; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; font-weight: 600; display: flex; align-items: center; gap: 10px; transition: color 0.3s; }
        .nav-link:hover { color: #fff; }
    </style>
</head>
<body>
    <a href="index.html" class="nav-link"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg> Return Home</a>
    
    <div class="legal-hero">
        <span class="badge">Master Agreement</span>
        <h1>Terms of Service</h1>
        <p>The operational framework governing your relationship with Evolvix Technologies.</p>
    </div>
    
    <div class="legal-container">
        <aside class="sidebar">
            <h3 style="color: #fff; margin-bottom: 20px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px;">Contents</h3>
            <ul>
                <li><a href="#acceptance">1. Acceptance of Terms</a></li>
                <li><a href="#ip">2. Intellectual Property Rights</a></li>
                <li><a href="#financial">3. Financial & Billing Policies</a></li>
                <li><a href="#liability">4. Limitation of Liability</a></li>
                <li><a href="#termination">5. Suspension & Termination</a></li>
                <li><a href="#governing">6. Governing Law & Jurisdiction</a></li>
            </ul>
        </aside>
        
        <main class="content-panel">
            <div class="highlight-box">
                <p style="margin:0; color: #fff; font-weight: 600;">By commissioning a project or utilizing the Client Portal, you are entering into a legally binding contract with Evolvix Technologies. Please review carefully.</p>
            </div>

            <h2 id="acceptance">1. Acceptance of Terms</h2>
            <p>These Terms of Service ("Terms") constitute a legally binding Master Services Agreement made between you, whether personally or on behalf of an entity ("Client"), and Evolvix Technologies. Access to the Client Portal implies explicit cryptographic acceptance of these terms.</p>

            <h2 id="ip">2. Intellectual Property & Code Ownership</h2>
            <p>Unless explicitly outlined in a custom MSA generated within the Client Portal:</p>
            <ul>
                <li><strong>Core Infrastructure:</strong> Evolvix retains all rights to proprietary backend architectures, AI algorithms, and deployment scripts utilized to construct the software.</li>
                <li><strong>Client Assets:</strong> Upon full execution of payment, the Client receives a perpetual, non-transferable license to utilize the finalized frontend interfaces and compiled binaries.</li>
            </ul>

            <h2 id="financial">3. Financial & Billing Policies</h2>
            <p>All enterprise invoices generated via the Client Portal adhere to strict NET-15 terms. Failure to remit payment within 15 days will result in:</p>
            <ul>
                <li>Immediate suspension of API access and server hosting.</li>
                <li>A late fee penalty compounding at 5% monthly on the outstanding balance.</li>
                <li>Subsequent referral to international debt collection agencies and credit bureaus if delinquent beyond 45 days.</li>
            </ul>

            <h2 id="liability">4. Limitation of Liability & Indemnification</h2>
            <p>Under no legal framework shall Evolvix Technologies, its directors, employees, or contractors be liable to you or any third party for any direct, indirect, consequential, exemplary, incidental, special, or punitive damages, including lost profit, lost revenue, or loss of data arising from your use of the delivered software. Our total liability shall explicitly never exceed the amount paid by you to us during the six (6) month period prior to any cause of action arising.</p>

            <h2 id="termination">5. Suspension & Termination</h2>
            <p>We reserve the right to unilaterally suspend, deactivate, or obliterate Client Portal access and associated server hosting if we detect:</p>
            <ul>
                <li>Breach of financial obligations.</li>
                <li>Attempted reverse-engineering of proprietary Evolvix APIs.</li>
                <li>Utilization of the delivered software for illicit, fraudulent, or illegal operations.</li>
            </ul>

            <h2 id="governing">6. Governing Law & Jurisdiction</h2>
            <p>These Terms shall be governed by and defined following the laws of the jurisdiction in which Evolvix Technologies operates. Evolvix Technologies and yourself irrevocably consent that the courts shall have exclusive jurisdiction to resolve any dispute which may arise in connection with these terms, specifically precluding class-action litigation.</p>
        </main>
    </div>
</body>
</html>'''

with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(privacy_content)

with open('terms.html', 'w', encoding='utf-8') as f:
    f.write(terms_content)

print('Legal pages totally overhauled to enterprise standard.')
