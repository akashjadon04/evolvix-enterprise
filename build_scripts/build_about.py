import re
import os

with open('c:/projects/evolvix/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract header (from start to </header>)
header_match = re.search(r'(?s)^.*?</header>', index_html)
header = header_match.group(0)

# Extract footer (from <footer> to end)
footer_match = re.search(r'(?s)<footer.*$', index_html)
footer = footer_match.group(0)

# Replace title in header
header = header.replace('<title>Evolvix Technologies | Enterprise Software & Scale</title>', '<title>Studio & Founder | Evolvix Technologies</title>')
# Replace nav link active state
header = header.replace('href="about.html" class="nav-link"', 'href="about.html" class="nav-link active"')
header = header.replace('href="index.html" class="nav-link active"', 'href="index.html" class="nav-link"')

about_main = """
    <style>
        /* ABOUT.HTML GOD MODE STYLES */
        .about-hero {
            padding: 10rem 0 6rem;
            background: radial-gradient(circle at center top, rgba(14, 116, 144, 0.15) 0%, transparent 60%);
            position: relative;
            overflow: hidden;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .about-hero::after {
            content: ''; position: absolute; inset: 0; 
            background: url('data:image/svg+xml;utf8,<svg width="40" height="40" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h40v40H0z" fill="none"/><circle cx="20" cy="20" r="1" fill="rgba(255,255,255,0.05)"/></svg>');
            z-index: 0; pointer-events: none;
        }
        .hero-title-group { position: relative; z-index: 2; text-align: center; }
        .hero-title-group h1 {
            font-family: 'Outfit'; font-size: clamp(3.5rem, 8vw, 6.5rem); font-weight: 900;
            line-height: 0.9; margin-bottom: 1.5rem; letter-spacing: -2px;
        }
        .text-outline {
            color: transparent;
            -webkit-text-stroke: 1px rgba(255,255,255,0.3);
        }
        
        .founder-section {
            padding: 8rem 0; position: relative; background: #020617;
        }
        .founder-grid {
            display: grid; grid-template-columns: 1fr 1.1fr; gap: 6rem; align-items: center;
        }
        .founder-image-wrapper {
            position: relative; border-radius: 24px; overflow: hidden;
            box-shadow: 0 40px 100px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.1);
        }
        .founder-image-wrapper img {
            width: 100%; height: auto; display: block;
            transition: transform 0.5s;
        }
        .founder-image-wrapper:hover img { transform: scale(1.05); }
        .founder-glare {
            position: absolute; inset: 0; background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, transparent 50%);
            pointer-events: none; z-index: 2; mix-blend-mode: overlay;
        }
        
        .founder-content h2 { font-family: 'Outfit'; font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 1.5rem; line-height: 1; }
        .founder-content p { font-size: 1.1rem; color: rgba(255,255,255,0.7); margin-bottom: 1.5rem; line-height: 1.7; }
        
        .standard-section { padding: 8rem 0; background: linear-gradient(180deg, #020617 0%, rgba(14, 116, 144, 0.05) 100%); }
        .standard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 4rem; }
        .standard-card {
            background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05);
            padding: 3rem; border-radius: 24px; position: relative; overflow: hidden;
            transition: 0.3s;
        }
        .standard-card:hover { transform: translateY(-10px); background: rgba(255,255,255,0.04); border-color: rgba(103,232,249,0.3); }
        .standard-card h3 { font-size: 1.8rem; font-family: 'Outfit'; margin-bottom: 1rem; color: #fff; }
        .standard-card .icon-3d { font-size: 3rem; margin-bottom: 1.5rem; display: inline-block; filter: drop-shadow(0 10px 10px rgba(103,232,249,0.2)); }
        
        .process-section { padding: 8rem 0; position: relative; }
        .process-line {
            display: flex; gap: 2rem; overflow-x: auto; padding-bottom: 2rem;
            scrollbar-width: thin; scrollbar-color: var(--c-brand-main) rgba(255,255,255,0.05);
        }
        .process-step {
            min-width: 350px; background: rgba(0,0,0,0.4); border: 1px solid rgba(255,255,255,0.05);
            padding: 3rem; border-radius: 24px; position: relative;
        }
        .step-num {
            position: absolute; top: 1rem; right: 1rem; font-family: 'JetBrains Mono';
            font-size: 4rem; font-weight: 900; color: rgba(255,255,255,0.03); line-height: 1;
        }

        .join-section {
            padding: 8rem 0; text-align: center; background: url('data:image/svg+xml;utf8,<svg width="40" height="40" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h40v40H0z" fill="none"/><circle cx="20" cy="20" r="1" fill="rgba(255,255,255,0.05)"/></svg>');
        }
        .join-box {
            max-width: 800px; margin: 0 auto; background: rgba(10, 15, 30, 0.8);
            backdrop-filter: blur(20px); border: 1px solid rgba(103,232,249,0.2);
            padding: 4rem; border-radius: 32px;
            box-shadow: 0 40px 100px rgba(0,0,0,0.5), inset 0 0 40px rgba(103,232,249,0.05);
        }

        @media (max-width: 900px) {
            .founder-grid { grid-template-columns: 1fr; gap: 3rem; }
            .founder-section, .standard-section, .process-section { padding: 4rem 0; }
            .process-step { min-width: 280px; }
            .join-box { padding: 2rem; }
        }
    </style>

    <main>
        <!-- HERO -->
        <section class="about-hero">
            <div class="container hero-title-group reveal">
                <h1>WE BUILD <span class="text-gradient">DIGITAL</span><br><span class="text-outline">EMPIRES</span></h1>
                <p style="font-size: 1.25rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                    We are not an agency. We are a digital product studio engineering the future of high-performance web experiences.
                </p>
            </div>
        </section>

        <!-- THE FOUNDER -->
        <section class="founder-section">
            <div class="container founder-grid">
                <div class="founder-image-wrapper reveal">
                    <div class="founder-glare"></div>
                    <img src="assets/akash.png" alt="Akash Jadon - Founder">
                </div>
                <div class="founder-content reveal delay-200">
                    <div style="font-family: 'JetBrains Mono'; color: var(--c-brand-light); margin-bottom: 1rem; letter-spacing: 2px; font-size: 0.8rem;">
                        // THE ARCHITECT
                    </div>
                    <h2>Vision Meets <span class="text-gradient">Execution.</span></h2>
                    <p>
                        "I founded Evolvix because I was tired of seeing brilliant brands held back by mediocre digital experiences. The web is flooded with templates and slow code."
                    </p>
                    <p>
                        "We do things differently. Every line of code, every pixel, and every animation is purposefully engineered to command attention and convert users into loyal customers. We build digital assets, not just websites."
                    </p>
                    <div style="margin-top: 3rem; display: flex; align-items: center; gap: 1rem;">
                        <div>
                            <div style="font-family: 'Outfit'; font-weight: 700; font-size: 1.2rem; color: #fff;">Akash Jadon</div>
                            <div style="color: var(--text-tertiary); font-size: 0.9rem;">Founder & Lead Engineer</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- THE EVOLVIX STANDARD (New Section 1) -->
        <section class="standard-section">
            <div class="container">
                <h2 style="font-family: 'Outfit'; font-size: clamp(2.5rem, 5vw, 4rem); text-align: center; margin-bottom: 1rem;">The Evolvix <span class="text-gradient">Standard</span></h2>
                <p style="text-align: center; color: var(--text-secondary); max-width: 600px; margin: 0 auto;">We refuse to compromise on quality. This is our baseline for every project.</p>
                
                <div class="standard-grid">
                    <div class="standard-card reveal">
                        <span class="icon-3d">⚡</span>
                        <h3>Millisecond Speed</h3>
                        <p style="color: var(--text-secondary); line-height: 1.6;">Our architectures load instantly. We optimize assets, leverage edge computing, and remove bloat to ensure a flawless experience.</p>
                    </div>
                    <div class="standard-card reveal delay-100">
                        <span class="icon-3d">🎨</span>
                        <h3>God Mode UI</h3>
                        <p style="color: var(--text-secondary); line-height: 1.6;">We design for emotion. Glassmorphism, 3D elements, micro-animations, and fluid layouts that make users say "wow".</p>
                    </div>
                    <div class="standard-card reveal delay-200">
                        <span class="icon-3d">🛡️</span>
                        <h3>Bulletproof Code</h3>
                        <p style="color: var(--text-secondary); line-height: 1.6;">Enterprise-grade security and scalability baked into the foundation. No spaghetti code, just pure engineering excellence.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- OUR PROCESS (New Section 2) -->
        <section class="process-section">
            <div class="container">
                <div style="font-family: 'JetBrains Mono'; color: var(--c-brand-light); margin-bottom: 1rem; letter-spacing: 2px; font-size: 0.8rem;">
                    // HOW WE WORK
                </div>
                <h2 style="font-family: 'Outfit'; font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 4rem;">The Alpha <span class="text-gradient">Protocol</span></h2>
                
                <div class="process-line">
                    <div class="process-step reveal">
                        <div class="step-num">01</div>
                        <h3 style="font-family: 'Outfit'; font-size: 1.5rem; margin-bottom: 1rem; color: #fff;">Deep Discovery</h3>
                        <p style="color: var(--text-secondary); line-height: 1.6;">We don't just ask what you want; we figure out what your business actually needs to crush the competition.</p>
                    </div>
                    <div class="process-step reveal delay-100">
                        <div class="step-num">02</div>
                        <h3 style="font-family: 'Outfit'; font-size: 1.5rem; margin-bottom: 1rem; color: #fff;">Visual Strategy</h3>
                        <p style="color: var(--text-secondary); line-height: 1.6;">Wireframes and high-fidelity mockups that establish a dominant visual hierarchy and premium aesthetic.</p>
                    </div>
                    <div class="process-step reveal delay-200">
                        <div class="step-num">03</div>
                        <h3 style="font-family: 'Outfit'; font-size: 1.5rem; margin-bottom: 1rem; color: #fff;">Alpha Engineering</h3>
                        <p style="color: var(--text-secondary); line-height: 1.6;">Writing the flawless code that brings the vision to life, integrating animations and backend logic.</p>
                    </div>
                    <div class="process-step reveal delay-300">
                        <div class="step-num">04</div>
                        <h3 style="font-family: 'Outfit'; font-size: 1.5rem; margin-bottom: 1rem; color: #fff;">Launch & Scale</h3>
                        <p style="color: var(--text-secondary); line-height: 1.6;">Deployment to edge networks. We monitor performance and hand over the keys to your new digital empire.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- OPEN POSITIONS -->
        <section class="join-section">
            <div class="container">
                <div class="join-box reveal">
                    <h2 style="font-family: 'Outfit'; font-size: 3rem; margin-bottom: 1rem; color: #fff;">Join the <span class="text-gradient">Vanguard.</span></h2>
                    <p style="color: var(--text-secondary); font-size: 1.1rem; margin-bottom: 3rem; max-width: 500px; margin-left: auto; margin-right: auto;">
                        We are always looking for elite designers and engineers who want to build the absolute best products on the web.
                    </p>
                    <a href="careers.html" class="btn btn-primary" style="padding: 1.25rem 2.5rem; font-size: 1.1rem;">
                        View Open Positions →
                    </a>
                </div>
            </div>
        </section>
    </main>
"""

with open('c:/projects/evolvix/about.html', 'w', encoding='utf-8') as f:
    f.write(header + about_main + footer)
