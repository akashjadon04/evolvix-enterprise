import os
import re

# 1. Update style.css
css_path = 'c:/projects/evolvix/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove .nav-menu::after rule from style.css
css = re.sub(r'\.nav-menu::after\{.*?\}', '', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Process all HTML files
html_dir = 'c:/projects/evolvix'
for file in os.listdir(html_dir):
    if file.endswith('.html'):
        path = os.path.join(html_dir, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove .nav-menu::after rule from inline styles if exists
        content = re.sub(r'\.nav-menu::after\s*\{.*?\}', '', content)
        
        # Add the real button to the end of nav-menu
        mobile_cta = '<li class="mobile-only-item" style="display:none;"><a href="contact.html" style="background:var(--c-brand-main);color:#fff;padding:1rem;border-radius:8px;font-weight:700;margin-top:1rem;display:block;text-align:center;text-decoration:none;">Start Project &rarr;</a></li>'
        
        # Add mobile-only-item display logic in inline styles if not there
        if 'mobile-only-item' not in content:
            style_block = '<style>@media (max-width:768px) { .mobile-only-item { display: block !important; } }</style>'
            content = content.replace('</head>', f'{style_block}\n</head>')
        
        # If the mobile-only-item is not already in the nav-menu, add it
        if 'mobile-only-item' not in content or mobile_cta not in content:
            content = re.sub(r'(</ul>)', f'{mobile_cta}\n\\1', content)
        
        # --- Contact Page Language Simplification ---
        if file == 'contact.html':
            content = content.replace('Initiate <br><span class="text-gradient">Project.</span>', 'Let\'s <br><span class="text-gradient">Talk.</span>')
            content = content.replace('You\'re one step away from building a dominant digital asset. Fill out the terminal, and our engineering team will evaluate your architecture needs.', 'We\'re ready to help you build something amazing. Fill out the form below and we will get back to you shortly.')
            content = content.replace('Project Inception Terminal', 'Tell us about yourself')
            content = content.replace('Enter your credentials to begin.', 'Fill out this simple form to get started.')
            content = content.replace('Initialize Uplink ⚡', 'Send Message ⚡')
            content = content.replace('// SECURE UPLINK //', '// GET IN TOUCH //')
            content = content.replace('UPLINK_READY', 'READY')
            content = content.replace('Uplink Established.', 'Message Sent.')
            content = content.replace('Your transmission has been securely received by Evolvix Core Intelligence. An architect will respond shortly.', 'Your message has been received. Our team will respond shortly.')
        
        # --- Pricing Page Layout Fix and New Section ---
        if file == 'pricing.html':
            # Fix Layout Bug (padding top overlap)
            content = content.replace('<section class="section text-center pricing-hero"', '<section class="section text-center pricing-hero" style="padding-top: 160px;"')
            
            # New Estimated Pricing Section
            if 'pricing-tiers-section' not in content:
                new_section = """
        <section class="pricing-tiers-section" style="padding: 6rem 0; background: #020617; border-top: 1px solid rgba(255,255,255,0.05);">
            <div class="container">
                <div style="text-align: center; margin-bottom: 4rem;" class="reveal">
                    <div style="font-family: 'JetBrains Mono'; color: #67e8f9; letter-spacing: 4px; font-size: 0.9rem; margin-bottom: 1.5rem; font-weight: 700;">// ALGORITHM ESTIMATES //</div>
                    <h2 style="font-family: 'Outfit'; font-size: clamp(2.5rem, 5vw, 4rem); color: #fff; margin-bottom: 1rem;">Estimated <span class="text-gradient">Investment</span></h2>
                    <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">Based on our historical project data, here is a rough outline of typical engagements. Exact pricing is determined after a strategy call.</p>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;" class="reveal delay-100">
                    
                    <!-- Tier 1 -->
                    <div style="background: linear-gradient(145deg, rgba(15,23,42,0.6), rgba(2,6,23,0.9)); border: 1px solid rgba(103,232,249,0.15); border-radius: 24px; padding: 3rem 2rem; position: relative; overflow: hidden; transition: 0.4s; transform-style: preserve-3d;" class="tier-card">
                        <div style="position: absolute; top: -50px; right: -50px; width: 150px; height: 150px; background: radial-gradient(circle, rgba(103,232,249,0.2) 0%, transparent 70%); filter: blur(20px);"></div>
                        <h3 style="font-family: 'Outfit'; font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">Web Architecture</h3>
                        <p style="color: rgba(255,255,255,0.5); font-size: 0.9rem; margin-bottom: 2rem; min-height: 45px;">High-performance corporate sites & digital assets.</p>
                        <div style="font-family: 'Outfit'; font-size: 3rem; font-weight: 900; color: #fff; margin-bottom: 2rem;">$10k<span style="font-size: 1rem; color: rgba(255,255,255,0.4); font-weight: 400;"> / avg</span></div>
                        <ul style="list-style: none; padding: 0; margin: 0 0 2rem; color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #38bdf8;">✓</span> Neuro-Design UI</li>
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #38bdf8;">✓</span> Sub-Second Loading</li>
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #38bdf8;">✓</span> 3D Graphics & WebGL</li>
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #38bdf8;">✓</span> SEO Foundation</li>
                        </ul>
                        <a href="contact.html" class="btn btn-secondary" style="width: 100%; text-align: center; border-color: rgba(103,232,249,0.3); color: #67e8f9;">Inquire Now</a>
                    </div>
                    
                    <!-- Tier 2 -->
                    <div style="background: linear-gradient(145deg, rgba(14,116,144,0.2), rgba(2,6,23,0.9)); border: 1px solid rgba(56,189,248,0.4); border-radius: 24px; padding: 3rem 2rem; position: relative; overflow: hidden; transition: 0.4s; box-shadow: 0 20px 50px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(103,232,249,0.2);" class="tier-card main-tier">
                        <div style="position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #0e7490, #67e8f9, #8b5cf6);"></div>
                        <div style="position: absolute; top: 1rem; right: 1rem; background: rgba(56,189,248,0.2); border: 1px solid rgba(56,189,248,0.5); padding: 0.2rem 0.8rem; border-radius: 20px; font-size: 0.7rem; color: #67e8f9; font-weight: 700;">MOST POPULAR</div>
                        <h3 style="font-family: 'Outfit'; font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">SaaS & Platforms</h3>
                        <p style="color: rgba(255,255,255,0.5); font-size: 0.9rem; margin-bottom: 2rem; min-height: 45px;">Complex web applications with robust backends.</p>
                        <div style="font-family: 'Outfit'; font-size: 3rem; font-weight: 900; color: #fff; margin-bottom: 2rem;">$35k<span style="font-size: 1rem; color: rgba(255,255,255,0.4); font-weight: 400;"> / avg</span></div>
                        <ul style="list-style: none; padding: 0; margin: 0 0 2rem; color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #38bdf8;">✓</span> Everything in Web</li>
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #38bdf8;">✓</span> React/Node.js Stack</li>
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #38bdf8;">✓</span> Cloud Infrastructure</li>
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #38bdf8;">✓</span> Enterprise Security</li>
                        </ul>
                        <a href="contact.html" class="btn btn-primary btn-cta-glow" style="width: 100%; text-align: center;">Initiate Build</a>
                    </div>
                    
                    <!-- Tier 3 -->
                    <div style="background: linear-gradient(145deg, rgba(15,23,42,0.6), rgba(2,6,23,0.9)); border: 1px solid rgba(139,92,246,0.25); border-radius: 24px; padding: 3rem 2rem; position: relative; overflow: hidden; transition: 0.4s; transform-style: preserve-3d;" class="tier-card">
                        <div style="position: absolute; bottom: -50px; left: -50px; width: 150px; height: 150px; background: radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%); filter: blur(20px);"></div>
                        <h3 style="font-family: 'Outfit'; font-size: 1.5rem; color: #fff; margin-bottom: 0.5rem;">Growth Retainer</h3>
                        <p style="color: rgba(255,255,255,0.5); font-size: 0.9rem; margin-bottom: 2rem; min-height: 45px;">Ongoing SEO, CRO, and feature development.</p>
                        <div style="font-family: 'Outfit'; font-size: 3rem; font-weight: 900; color: #fff; margin-bottom: 2rem;">$5k<span style="font-size: 1rem; color: rgba(255,255,255,0.4); font-weight: 400;"> / mo</span></div>
                        <ul style="list-style: none; padding: 0; margin: 0 0 2rem; color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #a78bfa;">✓</span> A/B Testing</li>
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #a78bfa;">✓</span> Technical SEO</li>
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #a78bfa;">✓</span> Priority Support</li>
                            <li style="margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="color: #a78bfa;">✓</span> Continuous Updates</li>
                        </ul>
                        <a href="contact.html" class="btn btn-secondary" style="width: 100%; text-align: center; border-color: rgba(139,92,246,0.4); color: #c4b5fd;">Apply for Retainer</a>
                    </div>
                    
                </div>
            </div>
            
            <style>
                .tier-card:hover { transform: translateY(-10px); border-color: rgba(103,232,249,0.4); box-shadow: 0 20px 40px rgba(0,0,0,0.6); }
                .main-tier:hover { border-color: #38bdf8; box-shadow: 0 30px 60px rgba(0,0,0,0.7), 0 0 20px rgba(56,189,248,0.2); }
            </style>
        </section>
                """
                content = content.replace('</main>', f'{new_section}\n    </main>')

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done fixing bugs and adding new sections.")
