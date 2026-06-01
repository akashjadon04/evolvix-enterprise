import re
import os

with open('c:/projects/evolnex/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

header_match = re.search(r'(?s)^.*?</header>', index_html)
header = header_match.group(0)

footer_match = re.search(r'(?s)<footer.*$', index_html)
footer = footer_match.group(0)

# Replace titles and nav state
header = header.replace('<title>Evolnex Technologies | Enterprise Software & Scale</title>', '<title>Start Project | Evolnex Technologies</title>')
# Contact button is usually a CTA, but let's just make sure Home isn't active
header = header.replace('href="index.html" class="nav-link active"', 'href="index.html" class="nav-link"')

contact_main = """
    <style>
        body { background: #020617; }
        .contact-hero {
            padding: 10rem 0 0rem;
            min-height: 100vh;
            display: flex; align-items: center; justify-content: center;
            position: relative; overflow: hidden;
            background: radial-gradient(circle at center 30%, rgba(14,116,144,0.1) 0%, #020617 70%);
        }
        .contact-bg-grid {
            position: absolute; inset: 0; pointer-events: none; z-index: 0;
            background-image: 
                linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
            background-size: 40px 40px;
            mask-image: radial-gradient(ellipse at top, black 20%, transparent 70%);
            -webkit-mask-image: radial-gradient(ellipse at top, black 20%, transparent 70%);
        }

        .contact-wrapper {
            width: 100%; max-width: 1400px; padding: 0 2rem; margin: 0 auto;
            position: relative; z-index: 2;
        }

        .contact-layout {
            display: grid; grid-template-columns: 1fr 1.2fr; gap: 4rem;
            align-items: stretch; margin-bottom: 6rem;
        }

        /* LEFT SIDE - VISUAL & TEXT */
        .contact-visual-panel {
            display: flex; flex-direction: column; justify-content: space-between;
        }
        .contact-heading h1 {
            font-family: 'Outfit'; font-size: clamp(3rem, 6vw, 5.5rem); font-weight: 900;
            line-height: 1; margin-bottom: 1.5rem; letter-spacing: -2px; color: #fff;
        }
        .contact-heading p {
            font-size: 1.15rem; color: rgba(255,255,255,0.6); max-width: 480px; line-height: 1.6;
        }
        
        .hologram-container {
            margin-top: 4rem; position: relative; height: 350px;
            border-radius: 24px; border: 1px solid rgba(103,232,249,0.15);
            background: linear-gradient(135deg, rgba(14,116,144,0.1), rgba(2,6,23,0.8));
            overflow: hidden; display: flex; align-items: center; justify-content: center;
            box-shadow: inset 0 0 40px rgba(103,232,249,0.05);
        }
        .hologram-container::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
            background: linear-gradient(90deg, transparent, #38bdf8, transparent);
            animation: scanline 4s linear infinite;
        }
        @keyframes scanline {
            0% { transform: translateY(-100%); }
            100% { transform: translateY(350px); }
        }
        
        .holo-globe { width: 250px; height: 250px; border-radius: 50%; border: 1px dashed rgba(103,232,249,0.3); position: relative; animation: spinGlobe 20s linear infinite; }
        .holo-globe::before { content: ''; position: absolute; inset: -20px; border-radius: 50%; border: 1px solid rgba(139,92,246,0.2); animation: spinGlobe 15s linear infinite reverse; }
        .holo-globe::after { content: ''; position: absolute; inset: -40px; border-radius: 50%; border: 1px dashed rgba(56,189,248,0.1); animation: spinGlobe 30s linear infinite; }
        @keyframes spinGlobe { 100% { transform: rotate(360deg); } }

        .holo-badge {
            position: absolute; top: 1.5rem; left: 1.5rem; background: rgba(2,6,23,0.8);
            border: 1px solid rgba(56,189,248,0.4); color: #38bdf8; font-family: 'JetBrains Mono';
            font-size: 0.7rem; padding: 0.4rem 1rem; border-radius: 20px; backdrop-filter: blur(10px);
        }

        /* RIGHT SIDE - GOD MODE FORM */
        .contact-form-panel {
            background: rgba(15,23,42,0.4); backdrop-filter: blur(30px); -webkit-backdrop-filter: blur(30px);
            border: 1px solid rgba(255,255,255,0.08); border-radius: 32px; padding: 4rem;
            box-shadow: 0 40px 100px -20px rgba(0,0,0,0.8), inset 0 0 0 1px rgba(255,255,255,0.02);
            position: relative;
        }
        /* Corner Brackets */
        .contact-form-panel::before { content: ''; position: absolute; top: 2rem; right: 2rem; width: 30px; height: 30px; border-top: 2px solid rgba(103,232,249,0.5); border-right: 2px solid rgba(103,232,249,0.5); }
        .contact-form-panel::after { content: ''; position: absolute; bottom: 2rem; left: 2rem; width: 30px; height: 30px; border-bottom: 2px solid rgba(103,232,249,0.5); border-left: 2px solid rgba(103,232,249,0.5); }

        .form-header { margin-bottom: 3rem; }
        .form-header h3 { font-family: 'Outfit'; font-size: 2rem; color: #fff; margin-bottom: 0.5rem; }
        .form-header p { color: rgba(255,255,255,0.5); font-size: 1rem; }

        .input-group-x { position: relative; margin-bottom: 2rem; }
        
        .grid-2-col { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
        
        .input-v2 {
            width: 100%; background: rgba(2,6,23,0.5); border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px; padding: 1.5rem 1.25rem 0.5rem; color: #fff; font-size: 1.05rem;
            outline: none; transition: 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        }
        textarea.input-v2 { resize: none; min-height: 140px; padding-top: 1.8rem; }
        
        .label-v2 {
            position: absolute; left: 1.25rem; top: 1.2rem; color: rgba(255,255,255,0.4);
            font-size: 1.05rem; pointer-events: none; transition: 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            font-family: 'Inter', sans-serif;
        }

        .input-v2:focus, .input-v2:not(:placeholder-shown) {
            border-color: #38bdf8; background: rgba(14,116,144,0.1);
            box-shadow: 0 0 0 4px rgba(56,189,248,0.1);
        }
        .input-v2:focus + .label-v2, .input-v2:not(:placeholder-shown) + .label-v2 {
            top: 0.4rem; font-size: 0.75rem; color: #67e8f9; font-weight: 700; letter-spacing: 1px;
        }

        .submit-btn {
            width: 100%; background: linear-gradient(135deg, #0e7490, #67e8f9);
            color: #020617; border: none; padding: 1.2rem; border-radius: 16px;
            font-family: 'Outfit'; font-size: 1.2rem; font-weight: 800; cursor: pointer;
            transition: 0.3s; position: relative; overflow: hidden;
            box-shadow: 0 10px 30px rgba(103,232,249,0.3);
        }
        .submit-btn:hover { transform: translateY(-2px); box-shadow: 0 15px 40px rgba(103,232,249,0.5); color: #fff; background: linear-gradient(135deg, #0891b2, #38bdf8); }
        
        @media (max-width: 1024px) {
            .contact-layout { grid-template-columns: 1fr; gap: 4rem; }
            .hologram-container { height: 250px; }
            .contact-form-panel { padding: 2.5rem; }
            .grid-2-col { grid-template-columns: 1fr; gap: 0; }
            .contact-heading h1 { font-size: clamp(3rem, 10vw, 4rem); }
        }
    </style>

    <main>
        <section class="contact-hero">
            <div class="contact-bg-grid"></div>
            
            <div class="contact-wrapper">
                <div class="contact-layout">
                    
                    <!-- LEFT VISUAL -->
                    <div class="contact-visual-panel reveal">
                        <div class="contact-heading">
                            <div style="font-family: 'JetBrains Mono'; color: #67e8f9; letter-spacing: 4px; font-size: 0.9rem; margin-bottom: 1.5rem; font-weight: 700;">// SECURE UPLINK //</div>
                            <h1>Initiate <br><span class="text-gradient">Project.</span></h1>
                            <p>You're one step away from building a dominant digital asset. Fill out the terminal, and our engineering team will evaluate your architecture needs.</p>
                        </div>
                        
                        <div class="hologram-container reveal delay-200">
                            <div class="holo-badge">UPLINK_READY</div>
                            <div class="holo-globe"></div>
                        </div>
                    </div>
                    
                    <!-- RIGHT FORM -->
                    <div class="contact-form-panel reveal delay-100">
                        <div class="form-header">
                            <h3>Project Inception Terminal</h3>
                            <p>Enter your credentials to begin.</p>
                        </div>

                        <!-- We use web3forms to silently process the backend via hidden iframe -->
                        <form action="https://api.web3forms.com/submit" method="POST" target="hidden_iframe" id="godContactForm" onsubmit="handleGodSubmit(event)">
                            <input type="hidden" name="access_key" value="453219ed-70bc-4e70-8b04-3be070c0f955">
                            <input type="hidden" name="subject" value="New Evolnex Project Lead">
                            <input type="hidden" name="from_name" value="Evolnex God Mode Terminal">

                            <div class="grid-2-col">
                                <div class="input-group-x">
                                    <input type="text" name="Name" id="godName" class="input-v2" placeholder=" " required>
                                    <label for="godName" class="label-v2">Full Name</label>
                                </div>
                                <div class="input-group-x">
                                    <input type="email" name="Email" id="godEmail" class="input-v2" placeholder=" " required>
                                    <label for="godEmail" class="label-v2">Work Email</label>
                                </div>
                            </div>
                            
                            <!-- Phone Number (Required by User) & Company -->
                            <div class="grid-2-col">
                                <div class="input-group-x">
                                    <input type="tel" name="Phone" id="godPhone" class="input-v2" placeholder=" " required>
                                    <label for="godPhone" class="label-v2">Phone Number</label>
                                </div>
                                <div class="input-group-x">
                                    <input type="text" name="Company" id="godCompany" class="input-v2" placeholder=" ">
                                    <label for="godCompany" class="label-v2">Company / Brand</label>
                                </div>
                            </div>

                            <div class="input-group-x">
                                <textarea name="Message" id="godMessage" class="input-v2" placeholder=" " required></textarea>
                                <label for="godMessage" class="label-v2">Project Details & Budget Range</label>
                            </div>

                            <button type="submit" class="submit-btn" id="godSubmitBtn">Initialize Uplink ⚡</button>
                        </form>
                    </div>

                </div>
            </div>
            
            <!-- Hidden iframe to prevent redirect -->
            <iframe name="hidden_iframe" id="hidden_iframe" style="display:none;"></iframe>
            
        </section>

        <script>
            function handleGodSubmit(e) {
                const btn = document.getElementById('godSubmitBtn');
                btn.innerHTML = 'Establishing Secure Connection...';
                btn.style.pointerEvents = 'none';
                btn.style.opacity = '0.7';
                
                // Reset form and show success state after short delay
                setTimeout(() => {
                    const panel = document.querySelector('.contact-form-panel');
                    panel.innerHTML = `
                        <div style="text-align:center; padding: 4rem 2rem;">
                            <div style="width: 80px; height: 80px; background: rgba(16,185,129,0.1); border: 2px solid #10b981; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; color: #10b981; margin: 0 auto 2rem; box-shadow: 0 0 30px rgba(16,185,129,0.3);">✓</div>
                            <h3 style="font-family: 'Outfit'; font-size: 2.5rem; color: #fff; margin-bottom: 1rem;">Uplink Established.</h3>
                            <p style="color: rgba(255,255,255,0.6); font-size: 1.1rem;">Your transmission has been securely received by Evolnex Core Intelligence. An architect will respond shortly.</p>
                        </div>
                    `;
                }, 1500);
            }
        </script>
    </main>
"""

with open('c:/projects/evolnex/contact.html', 'w', encoding='utf-8') as f:
    f.write(header + contact_main + footer)
