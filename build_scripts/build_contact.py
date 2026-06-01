import re

with open('c:/projects/evolnex/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract header (from start to </header>)
header_match = re.search(r'(?s)^.*?</header>', index_html)
header = header_match.group(0)

# Extract footer (from <footer> to end)
footer_match = re.search(r'(?s)<footer.*$', index_html)
footer = footer_match.group(0)

# Replace title in header
header = header.replace('<title>Evolnex Technologies | Enterprise Software & Scale</title>', '<title>Contact | Evolnex Technologies</title>')
# Replace nav link active state
header = header.replace('href="contact.html" class="nav-link"', 'href="contact.html" class="nav-link active"')
header = header.replace('href="index.html" class="nav-link active"', 'href="index.html" class="nav-link"')

contact_main = """
    <style>
        /* CONTACT OMEGA LAYOUT */
        body { background: #020617; overflow-x: hidden; padding-top: 80px; }

        .contact-omega-layout {
            display: grid; grid-template-columns: 1fr 1fr;
            min-height: calc(100vh - 80px);
            position: relative;
        }
        @media(max-width: 900px) { .contact-omega-layout { grid-template-columns: 1fr; } }

        /* LEFT PANEL: 3D GRAPHIC & INFO */
        .graphic-panel {
            position: relative; padding: 4rem;
            display: flex; flex-direction: column; justify-content: center;
            border-right: 1px solid rgba(255,255,255,0.05);
            background: radial-gradient(circle at left center, rgba(14, 116, 144, 0.15) 0%, transparent 70%);
            overflow: hidden;
        }
        .graphic-panel h1 { font-family: 'Outfit'; font-size: clamp(3rem, 5vw, 5rem); line-height: 1; margin-bottom: 1.5rem; color: #fff; }
        .text-gradient { background: linear-gradient(135deg, #fff, #67e8f9); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .graphic-panel p { color: rgba(255,255,255,0.6); font-size: 1.1rem; max-width: 400px; margin-bottom: 3rem; line-height: 1.6; }
        
        /* 3D LIVE GRAPHIC */
        .live-3d-scene {
            position: absolute; right: -100px; top: 50%; transform: translateY(-50%);
            width: 500px; height: 500px; pointer-events: none;
            perspective: 1000px;
        }
        .planet-core {
            position: absolute; inset: 100px;
            background: radial-gradient(circle, rgba(14, 116, 144, 0.4), transparent);
            border-radius: 50%; filter: blur(20px);
            animation: pulse-core 4s infinite alternate;
        }
        .ring {
            position: absolute; inset: 50px;
            border: 1px solid rgba(103,232,249,0.2);
            border-radius: 50%;
            transform-style: preserve-3d;
        }
        .ring.r1 { animation: spin 20s linear infinite; }
        .ring.r2 { animation: spin 15s linear infinite reverse; transform: rotateX(60deg); border-color: rgba(139,92,246,0.3); }
        .ring.r3 { animation: spin 25s linear infinite; transform: rotateY(60deg); }
        @keyframes spin { 100% { transform: rotateX(360deg) rotateY(360deg); } }
        @keyframes pulse-core { 100% { opacity: 0.5; transform: scale(1.1); } }

        .contact-info-cards { position: relative; z-index: 2; display: flex; flex-direction: column; gap: 1rem; }
        .holo-card {
            display: flex; align-items: center; gap: 1rem; padding: 1.5rem;
            background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05);
            border-radius: 16px; text-decoration: none; transition: all 0.3s;
            max-width: 350px; backdrop-filter: blur(10px);
        }
        .holo-card:hover { background: rgba(103,232,249,0.1); border-color: rgba(103,232,249,0.3); transform: translateX(10px); }
        .holo-card div:last-child { display: flex; flex-direction: column; }
        .holo-card .c-label { font-family: 'JetBrains Mono'; font-size: 0.7rem; color: rgba(255,255,255,0.5); }
        .holo-card .c-value { font-weight: 700; color: #fff; font-size: 1rem; }

        /* RIGHT PANEL: 3D FORM */
        .form-panel {
            padding: 4rem; display: flex; align-items: center; justify-content: center;
            background: url('data:image/svg+xml;utf8,<svg width="20" height="20" xmlns="http://www.w3.org/2000/svg"><circle cx="1" cy="1" r="1" fill="rgba(255,255,255,0.05)"/></svg>');
        }
        .premium-3d-form {
            width: 100%; max-width: 500px;
            background: rgba(10, 15, 30, 0.8);
            backdrop-filter: blur(24px);
            border-radius: 24px;
            padding: 3.5rem;
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 40px 80px rgba(0,0,0,0.8), inset 0 2px 2px rgba(255,255,255,0.1);
            transform: perspective(1000px) rotateY(-5deg);
            transition: transform 0.5s cubic-bezier(0.16,1,0.3,1);
        }
        .premium-3d-form:hover { transform: perspective(1000px) rotateY(0deg) translateY(-10px); }
        .premium-3d-form h3 { font-family: 'Outfit'; font-size: 2rem; margin-bottom: 2rem; color: #fff; }
        
        .floating-input-group { position: relative; margin-bottom: 1.5rem; }
        .floating-input {
            width: 100%; background: rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.1);
            border-radius: 12px; padding: 1.25rem 1rem 0.5rem; color: #fff; outline: none; transition: 0.3s;
            font-family: 'JetBrains Mono', sans-serif; font-size: 0.95rem;
        }
        .floating-input:focus { border-color: #67e8f9; box-shadow: 0 0 15px rgba(103,232,249,0.2); background: rgba(103,232,249,0.05); }
        .floating-label {
            position: absolute; left: 1rem; top: 1rem; color: rgba(255,255,255,0.4);
            pointer-events: none; transition: 0.3s; font-size: 1rem;
        }
        .floating-input:focus ~ .floating-label, .floating-input:not(:placeholder-shown) ~ .floating-label {
            top: 0.3rem; font-size: 0.7rem; color: #67e8f9; font-weight: 700;
        }

        .submit-btn-3d {
            width: 100%; padding: 1.2rem; background: linear-gradient(135deg, #0e7490, #67e8f9);
            border: none; border-radius: 12px; color: #020617; font-weight: 800; font-size: 1rem;
            cursor: pointer; position: relative; overflow: hidden;
            box-shadow: 0 10px 20px rgba(103,232,249,0.3), inset 0 -3px 0 rgba(0,0,0,0.2);
            transition: all 0.3s; margin-top: 1rem; font-family: 'Outfit', sans-serif;
        }
        .submit-btn-3d:hover { transform: translateY(-3px); box-shadow: 0 15px 30px rgba(103,232,249,0.5), inset 0 -3px 0 rgba(0,0,0,0.2); }
        .submit-btn-3d:active { transform: translateY(0); box-shadow: inset 0 3px 0 rgba(0,0,0,0.2); }
    </style>

    <main>
        <div class="contact-omega-layout">
            <div class="graphic-panel">
                <div class="live-3d-scene">
                    <div class="planet-core"></div>
                    <div class="ring r1"></div>
                    <div class="ring r2"></div>
                    <div class="ring r3"></div>
                </div>
                <h1>Let's Build.<br><span class="text-gradient">Together.</span></h1>
                <p>We partner with ambitious brands to build premium digital products. Reach out to schedule a consultation with our lead engineers.</p>
                
                <div class="contact-info-cards">
                    <a href="tel:+917668758238" class="holo-card">
                        <span style="font-size:1.5rem;">📞</span>
                        <div><span class="c-label">DIRECT LINE</span><span class="c-value">+91 7668758238</span></div>
                    </a>
                    <a href="mailto:evolvixtechnology@gmail.com" class="holo-card">
                        <span style="font-size:1.5rem;">✉️</span>
                        <div><span class="c-label">EMAIL</span><span class="c-value">evolvixtechnology@gmail.com</span></div>
                    </a>
                </div>
            </div>

            <div class="form-panel">
                <div class="premium-3d-form">
                    <iframe name="hidden_iframe" id="hidden_iframe" style="display:none;" onload="if(this.submitted) { document.getElementById('submit-btn').textContent='✓ REQUEST SENT'; document.getElementById('submit-btn').style.background='#10b981'; document.getElementById('submit-btn').style.color='#fff'; }"></iframe>
                    <form action="https://api.web3forms.com/submit" method="POST" target="hidden_iframe" onsubmit="document.getElementById('hidden_iframe').submitted=true; document.getElementById('submit-btn').textContent='SENDING...';">
                        <input type="hidden" name="access_key" value="453219ed-70bc-4e70-8b04-3be070c0f955">
                        <input type="hidden" name="_subject" value="New Contact Form Submission">
                        
                        <h3>Start Your Project</h3>
                        
                        <div class="floating-input-group">
                            <input type="text" name="name" class="floating-input" placeholder=" " required>
                            <label class="floating-label">Full Name</label>
                        </div>
                        
                        <div class="floating-input-group">
                            <input type="email" name="email" class="floating-input" placeholder=" " required>
                            <label class="floating-label">Email Address</label>
                        </div>
                        
                        <div class="floating-input-group">
                            <input type="text" name="company" class="floating-input" placeholder=" ">
                            <label class="floating-label">Company / Brand (Optional)</label>
                        </div>
                        
                        <div class="floating-input-group">
                            <textarea name="message" class="floating-input" rows="4" placeholder=" " required></textarea>
                            <label class="floating-label">Project Details</label>
                        </div>
                        
                        <button type="submit" id="submit-btn" class="submit-btn-3d">SEND REQUEST</button>
                    </form>
                </div>
            </div>
        </div>
    </main>
"""

with open('c:/projects/evolnex/contact.html', 'w', encoding='utf-8') as f:
    f.write(header + contact_main + footer)
