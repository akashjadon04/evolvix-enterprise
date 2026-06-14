const fs = require("fs");
let c = fs.readFileSync("index.html", "utf8");

// Very safe, explicit string replacements for corrupted Unicode
c = c.split("Accepting New Projects \uFFFD?\" 2026").join("Accepting New Projects — 2026");
c = c.split("Let's Talk \uFFFD+'").join("Let's Talk →");
c = c.split(">Start Project \uFFFD+`</button>").join(">Start Project →</button>");
c = c.split("From Zero to Launch \uFFFDA").join("From Zero to Launch —");
c = c.split("Ac 2026").join("© 2026");
c = c.split("Skip t\uFFFDo").join("Skip to");
c = c.split("\uFFFDsT\uFFFD").join("");

// Fix buttons and lists globally (the previous commit had some mangled bytes replacing unicode)
c = c.replace(/â†’/g, "→");
c = c.replace(/âš™ï¸ /g, "⚙️");
c = c.replace(/âš¡/g, "⚡");
c = c.replace(/Ã—/g, "×");
c = c.replace(/âœ“/g, "✓");
c = c.replace(/ðŸŽ¨/g, "🎨");
c = c.replace(/â€”/g, "—");
c = c.replace(/ðŸ“±/g, "📱");
c = c.replace(/ðŸ” /g, "🔍");
c = c.replace(/ðŸ”—/g, "🔗");
c = c.replace(/â˜°/g, "☰");

// Add native CSS smooth scrolling
c = c.replace("html,body{", "html{scroll-behavior:smooth;}html,body{");

// Restore Three.js instead of native canvas
const threeScript = '<script defer src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>';
c = c.replace('<!-- Three.js removed: unused, saves 600KB -->', threeScript);

// Fix the exact footer
const footerStart = c.indexOf('<footer');
const footerEnd = c.indexOf('</footer>');
if (footerStart > 0 && footerEnd > 0) {
    const before = c.substring(0, footerStart);
    const after = c.substring(footerEnd + 9);
    const footer = `<footer class="footer" role="contentinfo">
  <div aria-hidden="true" class="footer-bg-text">EVOLNEX</div>
  <div class="container" style="position:relative;z-index:2;">
    <div class="footer-status-bar">
      <div class="footer-status-item"><span class="status-dot-green"></span>All Systems Operational</div>
      <div class="footer-status-sep"></div>
      <div class="footer-status-item"><span class="status-dot-blue"></span>Accepting New Projects &mdash; 2026</div>
      <div class="footer-status-sep"></div>
      <div class="footer-status-item"><span class="status-dot-green"></span>Response Time &lt; 24hrs</div>
      <div style="margin-left:auto;"><a href="/contact" style="font-size:.78rem;color:var(--c-brand-light);text-decoration:none;font-weight:700;">Let's Talk &rarr;</a></div>
    </div>
  </div>
  <div class="container footer-grid">
    <div>
      <a href="/" style="display:inline-block;"><img alt="Evolnex Technologies" class="footer-evolnex-logo" height="60" loading="lazy" src="assets/evolnex.webp" width="140"/></a>
      <p style="font-size:.92rem;margin-bottom:1.5rem;color:var(--text-secondary);line-height:1.7;">Evolnex Technologies &mdash; a digital product studio that builds high-performance websites, apps, and SaaS platforms for founders who refuse to be ordinary.</p>
      <div class="footer-socials">
        <a aria-label="LinkedIn" class="social-btn" href="https://www.linkedin.com/company/evolnex" rel="noopener noreferrer" target="_blank">in</a>
        <a aria-label="X (Twitter)" class="social-btn" href="https://x.com/evolnex" rel="noopener noreferrer" target="_blank">x</a>
        <a aria-label="Instagram" class="social-btn" href="https://www.instagram.com/evolnextechnologies/" rel="noopener noreferrer" target="_blank">ig</a>
        <a aria-label="YouTube" class="social-btn" href="https://youtube.com/@evolnex" rel="noopener noreferrer" target="_blank">yt</a>
        <a aria-label="Facebook" class="social-btn" href="https://facebook.com/evolnex" rel="noopener noreferrer" target="_blank">fb</a>
      </div>
      <address style="margin-top:1.5rem;font-size:.82rem;color:var(--text-secondary);line-height:1.9;font-style:normal;">
        <strong style="color:var(--text-primary);display:block;margin-bottom:.25rem;">Evolnex Technologies</strong>
        GNA University Campus, Phagwara, Punjab 144401, India<br/>
        <a href="tel:+917668758238" style="color:var(--c-brand-light);text-decoration:none;">+91 76687 58238</a>
      </address>
    </div>
    <div>
      <div class="footer-heading">Services</div>
      <a class="footer-link" href="/services">Web Development</a>
      <a class="footer-link" href="/services">App Development</a>
      <a class="footer-link" href="/services">SaaS Platforms</a>
      <a class="footer-link" href="/services">Technical SEO</a>
      <a class="footer-link" href="/services">Digital Marketing</a>
    </div>
    <div>
      <div class="footer-heading">Company</div>
      <a class="footer-link" href="/about">About Us</a>
      <a class="footer-link" href="/case-studies">Our Work</a>
      <a class="footer-link" href="/pricing">Pricing</a>
      <a class="footer-link" href="/careers">Careers</a>
      <a class="footer-link" href="/contact">Contact</a>
    </div>
    <div>
      <div class="footer-heading">Legal</div>
      <a class="footer-link" href="/privacy">Privacy Policy</a>
      <a class="footer-link" href="/terms">Terms of Service</a>
      <div class="footer-heading" style="margin-top:2rem;">Contact</div>
      <a class="footer-link" href="tel:+917668758238">&#128222; +91 7668758238</a>
      <a class="footer-link" href="mailto:contact@evolnex.digital">&#9993; contact@evolnex.digital</a>
    </div>
  </div>
  <div class="container copyright">
    <div class="copyright-left">&copy; 2026 Evolnex Technologies. All rights reserved.</div>
    <a class="owner-signature" href="/about">Crafted by Akash Jadon</a>
  </div>
</footer>`;
    c = before + footer + after;
}

fs.writeFileSync("index.html", c, "utf8");
console.log("Done");
