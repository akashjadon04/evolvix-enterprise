import re
import os

with open('c:/projects/evolvix/index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

header_match = re.search(r'(?s)^.*?</header>', index_html)
header = header_match.group(0)

footer_match = re.search(r'(?s)<footer.*$', index_html)
footer = footer_match.group(0)

header = header.replace('<title>Evolvix Technologies | Enterprise Software & Scale</title>', '<title>Studio & Founder | Evolvix Technologies</title>')
header = header.replace('href="about.html" class="nav-link"', 'href="about.html" class="nav-link active"')
header = header.replace('href="index.html" class="nav-link active"', 'href="index.html" class="nav-link"')

about_main = """
    <style>
        /* ABOUT.HTML GOD MODE STYLES - EXCLUSIVE & NON-REPEATING */
        body { background: #020617; }
        
        /* 1. Cyber Grid Hero */
        .about-hero-v2 {
            padding: 12rem 0 8rem;
            position: relative;
            background: #020617;
            overflow: hidden;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .cyber-grid {
            position: absolute; inset: -50%; top: 0;
            background-image: 
                linear-gradient(rgba(103,232,249,0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(103,232,249,0.05) 1px, transparent 1px);
            background-size: 50px 50px;
            transform: perspective(500px) rotateX(60deg) translateY(-100px) translateZ(-200px);
            animation: gridMove 20s linear infinite;
            z-index: 0; pointer-events: none;
            mask-image: radial-gradient(ellipse at center, black 0%, transparent 80%);
            -webkit-mask-image: radial-gradient(ellipse at center, black 0%, transparent 80%);
        }
        @keyframes gridMove {
            0% { transform: perspective(500px) rotateX(60deg) translateY(0) translateZ(-200px); }
            100% { transform: perspective(500px) rotateX(60deg) translateY(50px) translateZ(-200px); }
        }
        .hero-title-group { position: relative; z-index: 2; text-align: center; }
        .hero-title-group h1 {
            font-family: 'Outfit'; font-size: clamp(4rem, 10vw, 8rem); font-weight: 900;
            line-height: 0.85; margin-bottom: 1.5rem; letter-spacing: -3px;
            text-transform: uppercase; color: #fff;
            text-shadow: 0 20px 40px rgba(0,0,0,0.5);
        }
        .text-hollow {
            color: transparent;
            -webkit-text-stroke: 2px rgba(255,255,255,0.15);
            background: url('data:image/svg+xml;utf8,<svg width="40" height="40" xmlns="http://www.w3.org/2000/svg"><path d="M0 0h40v40H0z" fill="none"/><circle cx="20" cy="20" r="1" fill="rgba(103,232,249,0.3)"/></svg>');
            -webkit-background-clip: text; background-clip: text;
        }

        /* 2. Founder Profile HUD */
        .founder-hud-section { padding: 10rem 0; position: relative; background: #020617; overflow: hidden; }
        .founder-hud-section::before {
            content: ''; position: absolute; right: -20%; top: 20%; width: 60%; height: 60%;
            background: radial-gradient(circle, rgba(139,92,246,0.1) 0%, transparent 70%); filter: blur(60px); z-index: 0; pointer-events: none;
        }
        .founder-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; position: relative; z-index: 2; }
        
        .hud-frame {
            position: relative; padding: 2rem; border-radius: 30px;
            background: rgba(15,23,42,0.4); border: 1px solid rgba(103,232,249,0.15);
            box-shadow: 0 50px 100px -20px rgba(0,0,0,0.8), inset 0 0 0 1px rgba(255,255,255,0.02);
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        }
        /* Corner Accents */
        .hud-frame::before, .hud-frame::after { content: ''; position: absolute; width: 40px; height: 40px; pointer-events: none; transition: 0.5s; }
        .hud-frame::before { top: -2px; left: -2px; border-top: 3px solid #67e8f9; border-left: 3px solid #67e8f9; border-radius: 30px 0 0 0; }
        .hud-frame::after { bottom: -2px; right: -2px; border-bottom: 3px solid #8b5cf6; border-right: 3px solid #8b5cf6; border-radius: 0 0 30px 0; }
        .hud-frame:hover::before { width: 100%; height: 100%; border-radius: 30px; opacity: 0.3; }
        
        .hud-image-box {
            position: relative; border-radius: 20px; overflow: hidden;
            background: linear-gradient(180deg, rgba(255,255,255,0.05), transparent);
        }
        .hud-image-box img { width: 100%; height: auto; display: block; filter: contrast(1.1) saturate(1.1); mix-blend-mode: luminosity; transition: 0.7s cubic-bezier(0.16, 1, 0.3, 1); }
        .hud-frame:hover img { mix-blend-mode: normal; transform: scale(1.03); }
        
        .hud-data-points { position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 10; }
        .data-badge {
            position: absolute; background: rgba(2,6,23,0.8); border: 1px solid rgba(103,232,249,0.3);
            color: #67e8f9; font-size: 0.7rem; font-family: 'JetBrains Mono', monospace; font-weight: 700;
            padding: 0.4rem 1rem; border-radius: 20px; backdrop-filter: blur(10px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.5); opacity: 0; transform: translateY(10px); transition: 0.5s;
        }
        .hud-frame:hover .data-badge { opacity: 1; transform: translateY(0); }
        .badge-1 { top: 10%; right: -5%; }
        .badge-2 { bottom: 15%; left: -5%; border-color: rgba(139,92,246,0.4); color: #c4b5fd; }
        
        /* Typography for Founder Text */
        .founder-text-block h2 { font-family: 'Outfit'; font-size: clamp(2.5rem, 4vw, 4rem); line-height: 1.1; margin-bottom: 2rem; color: #fff; }
        .founder-text-block p { font-size: 1.15rem; color: rgba(255,255,255,0.65); line-height: 1.8; margin-bottom: 1.5rem; }
        .sign-off { font-family: 'Outfit'; font-weight: 800; font-size: 1.5rem; color: #fff; margin-top: 2rem; }
        .sign-off span { display: block; font-family: 'Inter'; font-weight: 500; font-size: 0.9rem; color: var(--c-brand-light); text-transform: uppercase; letter-spacing: 2px; margin-top: 0.2rem; }

        /* 3. The Architecture Grid (New Standard section) */
        .architecture-section { padding: 8rem 0; background: #020617; border-top: 1px solid rgba(255,255,255,0.02); }
        .arch-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.05); border-radius: 30px; overflow: hidden; margin-top: 4rem; }
        .arch-panel { background: #0b1120; padding: 4rem 3rem; position: relative; transition: 0.5s; }
        .arch-panel:hover { background: #0f172a; }
        .arch-panel::after {
            content: ''; position: absolute; inset: 0; background: radial-gradient(circle at top right, rgba(103,232,249,0.1), transparent 50%); opacity: 0; transition: 0.5s; pointer-events: none;
        }
        .arch-panel:hover::after { opacity: 1; }
        .arch-icon {
            width: 60px; height: 60px; border-radius: 16px; background: rgba(15,23,42,0.8);
            border: 1px solid rgba(103,232,249,0.2); display: flex; align-items: center; justify-content: center;
            font-size: 1.8rem; color: #67e8f9; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .arch-panel h3 { font-family: 'Outfit'; font-size: 1.8rem; color: #fff; margin-bottom: 1rem; }
        .arch-panel p { color: rgba(255,255,255,0.5); line-height: 1.7; font-size: 1rem; }

        /* 4. The Infinity Protocol (Process) */
        .infinity-process { padding: 10rem 0; position: relative; background: radial-gradient(ellipse at center, rgba(14,116,144,0.05) 0%, #020617 70%); }
        .timeline-container { position: relative; max-width: 800px; margin: 4rem auto 0; }
        .timeline-line { position: absolute; left: 50%; top: 0; bottom: 0; width: 2px; background: rgba(255,255,255,0.05); transform: translateX(-50%); }
        .timeline-glow { position: absolute; left: 50%; top: 0; height: 100%; width: 2px; background: linear-gradient(180deg, #38bdf8, #8b5cf6); transform: translateX(-50%); filter: drop-shadow(0 0 10px #67e8f9); clip-path: polygon(0 0, 100% 0, 100% 0, 0 0); transition: clip-path 1s; }
        
        .timeline-item { position: relative; display: flex; justify-content: space-between; align-items: center; margin-bottom: 6rem; width: 100%; }
        .timeline-item:last-child { margin-bottom: 0; }
        .timeline-content { width: 45%; background: rgba(15,23,42,0.4); border: 1px solid rgba(255,255,255,0.05); padding: 3rem; border-radius: 24px; backdrop-filter: blur(10px); transition: 0.4s; }
        .timeline-item:nth-child(even) .timeline-content { margin-left: auto; }
        .timeline-content:hover { border-color: rgba(103,232,249,0.3); transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
        .timeline-dot { position: absolute; left: 50%; top: 50%; width: 20px; height: 20px; background: #020617; border: 4px solid #38bdf8; border-radius: 50%; transform: translate(-50%, -50%); z-index: 2; box-shadow: 0 0 20px rgba(56,189,248,0.5); }
        
        .t-num { font-family: 'JetBrains Mono'; font-size: 1rem; color: #67e8f9; margin-bottom: 0.5rem; display: block; font-weight: 700; letter-spacing: 2px; }
        .timeline-content h3 { font-family: 'Outfit'; font-size: 1.8rem; color: #fff; margin-bottom: 1rem; }
        .timeline-content p { color: rgba(255,255,255,0.6); line-height: 1.6; }

        /* 5. Recruitment Command Center */
        .command-center { padding: 8rem 0; border-top: 1px solid rgba(255,255,255,0.05); background: #020617; }
        .cc-box {
            background: url('data:image/svg+xml;utf8,<svg width="20" height="20" xmlns="http://www.w3.org/2000/svg"><rect width="20" height="20" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/></svg>'), rgba(10,15,30,0.8);
            border: 1px solid rgba(139,92,246,0.3); padding: 6rem 4rem; border-radius: 30px; text-align: center; position: relative; overflow: hidden;
        }
        .cc-box::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent, #8b5cf6, transparent); }
        .pulse-badge { display: inline-flex; align-items: center; gap: 8px; background: rgba(139,92,246,0.1); border: 1px solid rgba(139,92,246,0.4); padding: 8px 20px; border-radius: 30px; color: #c4b5fd; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 2rem; }
        .pulse-dot { width: 8px; height: 8px; background: #a78bfa; border-radius: 50%; box-shadow: 0 0 10px #a78bfa; animation: pulse-green 1.5s infinite; }
        
        @media (max-width: 900px) {
            .founder-grid { grid-template-columns: 1fr; gap: 3rem; }
            .arch-grid { grid-template-columns: 1fr; gap: 2px; }
            .timeline-line, .timeline-glow { left: 0; }
            .timeline-item { justify-content: flex-end; }
            .timeline-content { width: 90%; }
            .timeline-dot { left: 0; }
            .hud-frame { padding: 1rem; }
        }
    </style>

    <main>
        <!-- HERO -->
        <section class="about-hero-v2">
            <div class="cyber-grid"></div>
            <div class="container hero-title-group reveal">
                <div style="font-family: 'JetBrains Mono'; color: #67e8f9; letter-spacing: 4px; font-size: 0.9rem; margin-bottom: 2rem; font-weight: 700;">// EVOLVIX CORE //</div>
                <h1>WE BUILD <span class="text-hollow">DIGITAL</span><br>EMPIRES</h1>
                <p style="font-size: 1.25rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto;">
                    We are not an agency. We are an elite product studio engineering the future of high-performance web architecture.
                </p>
            </div>
        </section>

        <!-- THE FOUNDER -->
        <section class="founder-hud-section">
            <div class="container founder-grid">
                <div class="hud-frame reveal">
                    <div class="hud-image-box">
                        <img src="assets/akash.png" alt="Akash Jadon - Founder">
                        <div class="hud-data-points">
                            <div class="data-badge badge-1">ID: ARCHITECT-01</div>
                            <div class="data-badge badge-2">STATUS: DEPLOYING</div>
                        </div>
                    </div>
                </div>
                <div class="founder-text-block reveal delay-200">
                    <h2>Vision Meets <span class="text-gradient">Execution.</span></h2>
                    <p>
                        "I founded Evolvix because I was exhausted by seeing brilliant brands crippled by mediocre digital experiences. The web is flooded with lazy templates and bloated code."
                    </p>
                    <p>
                        "We refuse to operate on that level. Every line of code, every pixel, and every animation is engineered to command attention and crush your competition. We don't just build websites; we build scalable digital assets."
                    </p>
                    <div class="sign-off">
                        Akash Jadon
                        <span>Founder & Lead Engineer</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- THE ARCHITECTURE GRID -->
        <section class="architecture-section">
            <div class="container">
                <div style="text-align: center;" class="reveal">
                    <h2 style="font-family: 'Outfit'; font-size: clamp(2.5rem, 5vw, 4rem); color: #fff; margin-bottom: 1rem;">The Engineering <span class="text-gradient">Standard</span></h2>
                    <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">We don't compromise. This is the baseline architecture for every product we ship.</p>
                </div>
                
                <div class="arch-grid reveal delay-100">
                    <div class="arch-panel">
                        <div class="arch-icon">⚡</div>
                        <h3>Sub-Second Load</h3>
                        <p>Our architectures are built for absolute velocity. Edge-network deployment, optimized assets, and zero bloat guarantee immediate rendering.</p>
                    </div>
                    <div class="arch-panel">
                        <div class="arch-icon">👁️</div>
                        <h3>Neuro-Design UI</h3>
                        <p>We design for human psychology. Fluid micro-interactions, glassmorphism, and aggressive visual hierarchy that triggers emotional conversion.</p>
                    </div>
                    <div class="arch-panel">
                        <div class="arch-icon">🛡️</div>
                        <h3>Fort Knox Code</h3>
                        <p>Enterprise-grade scalability and security baked into the foundation. Pristine, maintainable code structures ready to handle millions of users.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- INFINITY PROTOCOL -->
        <section class="infinity-process">
            <div class="container">
                <div style="text-align: center;" class="reveal">
                    <h2 style="font-family: 'Outfit'; font-size: clamp(2.5rem, 5vw, 4rem); color: #fff; margin-bottom: 1rem;">The Alpha <span class="text-gradient">Protocol</span></h2>
                    <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">Our systematic approach to market domination.</p>
                </div>
                
                <div class="timeline-container">
                    <div class="timeline-line"></div>
                    <div class="timeline-glow" id="scrollGlow"></div>
                    
                    <div class="timeline-item reveal">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <span class="t-num">PHASE // 01</span>
                            <h3>Deep Reconnaissance</h3>
                            <p>We don't just take orders. We analyze your market, your competitors, and your bottlenecks to architect a superior strategy.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-item reveal">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <span class="t-num">PHASE // 02</span>
                            <h3>Visual Dominance</h3>
                            <p>Crafting high-fidelity prototypes that establish an immediate, premium aesthetic to separate you from average competitors.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-item reveal">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <span class="t-num">PHASE // 03</span>
                            <h3>Core Engineering</h3>
                            <p>Translating design into flawless, high-performance code. Integrating complex animations, backend logic, and robust databases.</p>
                        </div>
                    </div>
                    
                    <div class="timeline-item reveal">
                        <div class="timeline-dot"></div>
                        <div class="timeline-content">
                            <span class="t-num">PHASE // 04</span>
                            <h3>Deployment & Scale</h3>
                            <p>Global launch on edge servers. We secure the perimeter, optimize for absolute speed, and hand you the keys to the empire.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- COMMAND CENTER (Open Positions) -->
        <section class="command-center">
            <div class="container">
                <div class="cc-box reveal">
                    <div class="pulse-badge">
                        <div class="pulse-dot"></div> RECRUITMENT ACTIVE
                    </div>
                    <h2 style="font-family: 'Outfit'; font-size: clamp(2.5rem, 4vw, 3.5rem); margin-bottom: 1rem; color: #fff;">Join the <span style="color: #c4b5fd;">Vanguard.</span></h2>
                    <p style="color: rgba(255,255,255,0.6); font-size: 1.15rem; margin-bottom: 3rem; max-width: 600px; margin-left: auto; margin-right: auto;">
                        We are actively recruiting elite designers and engineers. If you refuse to write average code, your seat is ready.
                    </p>
                    <a href="careers.html" class="btn btn-primary" style="padding: 1.25rem 3rem; font-size: 1.1rem; background: #8b5cf6; border-color: #a78bfa; box-shadow: 0 0 30px rgba(139,92,246,0.4);">
                        View Open Terminals →
                    </a>
                </div>
            </div>
        </section>

        <script>
            // Timeline Glow Scroll Effect
            window.addEventListener('scroll', () => {
                const timeline = document.querySelector('.timeline-container');
                const glow = document.getElementById('scrollGlow');
                if(!timeline || !glow) return;
                
                const rect = timeline.getBoundingClientRect();
                const windowHeight = window.innerHeight;
                
                // Calculate how much of the timeline is visible
                let progress = 0;
                if (rect.top < windowHeight / 2) {
                    progress = (windowHeight / 2 - rect.top) / rect.height;
                }
                
                progress = Math.max(0, Math.min(1, progress));
                glow.style.clipPath = `polygon(0 0, 100% 0, 100% ${progress * 100}%, 0 ${progress * 100}%)`;
            });
        </script>
    </main>
"""

with open('c:/projects/evolvix/about.html', 'w', encoding='utf-8') as f:
    f.write(header + about_main + footer)
