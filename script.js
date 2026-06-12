"use strict";
const MathUtils = {
    lerp: (start, end, amt) => (1 - amt) * start + amt * end
};

class CardTilt {
    constructor(el) {
        this.el = el;
        this._r = null;
        this._w = 0;
        this._h = 0;
        this.el.addEventListener("mouseenter", () => {
            this._r = this.el.getBoundingClientRect();
            this._w = this._r.width;
            this._h = this._r.height;
        });
        this.el.addEventListener("mousemove", (e) => this.handleMove(e));
        this.el.addEventListener("mouseleave", () => this.handleLeave());
    }
    handleMove(e) {
        if (!this._r) return;
        const rect = this._r;
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const tiltX = (y - this._h / 2) / this._h * -20;
        const tiltY = (x - this._w / 2) / this._w * 20;
        this.el.style.transform = `perspective(1000px) scale(1.05) rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
        this.el.style.setProperty("--mouse-x", `${x}px`);
        this.el.style.setProperty("--mouse-y", `${y}px`);
    }
    handleLeave() {
        this.el.style.transform = "perspective(1000px) scale(1) rotateX(0) rotateY(0)";
        this._r = null;
    }
}

class PageLoader {
    constructor() {
        this.links = document.querySelectorAll("a");
        this.overlay = document.createElement("div");
        this.overlay.style.cssText = `
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: #000; z-index: 99999; transform: scaleY(0);
            transform-origin: bottom; transition: transform 0.6s cubic-bezier(0.87, 0, 0.13, 1);
        `;
        document.body.appendChild(this.overlay);
        this.init();
    }
    init() {
        window.addEventListener("pageshow", () => {
            this.overlay.style.transformOrigin = "top";
            this.overlay.style.transform = "scaleY(0)";
        });
        this.links.forEach(link => {
            if (link.hostname === window.location.hostname && (link.getAttribute("href") || "").indexOf("#") === -1 && link.target !== "_blank") {
                link.addEventListener("click", e => {
                    e.preventDefault();
                    const url = link.getAttribute("href");
                    this.transitionTo(url);
                });
            }
        });
    }
    transitionTo(url) {
        this.overlay.style.transformOrigin = "bottom";
        this.overlay.style.transform = "scaleY(1)";
        setTimeout(() => {
            window.location.href = url;
        }, 600);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".card, .glass-card, .tilt-card, .service-card, .portfolio-card").forEach(el => new CardTilt(el));
    new PageLoader();

    const navToggle = document.querySelector(".nav-toggle");
    const navMenu = document.querySelector(".nav-menu");
    if (navToggle && navMenu) {
        navToggle.addEventListener("click", () => {
            navMenu.classList.toggle("active");
            navToggle.classList.toggle("active");
            navToggle.innerHTML = navMenu.classList.contains("active") ? "✕" : "☰";
        });
        document.querySelectorAll(".nav-link").forEach(link => {
            link.addEventListener("click", () => {
                navMenu.classList.remove("active");
                navToggle.innerHTML = "☰";
            });
        });
    }
    console.log("SUMMITFORGE V6: GOD MODE ENGINE ACTIVE");
});

/* ─── Premium Magnetic Trailing Cursor ─── */
(function() {
    if (!window.matchMedia('(pointer:fine)').matches) return; // Only desktop
    
    // Main cursor dot
    var c = document.createElement('div');
    c.style.cssText = 'position:fixed;top:0;left:0;width:8px;height:8px;background:#38bdf8;border-radius:50%;pointer-events:none;z-index:999999;transform:translate(-50%,-50%);transition:transform 0.1s;';
    document.body.appendChild(c);

    // Trail elements
    var trails = [];
    var numTrails = 6;
    for (var i = 0; i < numTrails; i++) {
        var t = document.createElement('div');
        t.style.cssText = `position:fixed;top:0;left:0;width:${24 - i * 3}px;height:${24 - i * 3}px;border:1px solid rgba(56,189,248,${0.6 - i * 0.1});border-radius:50%;pointer-events:none;z-index:${999998 - i};transform:translate(-50%,-50%);`;
        document.body.appendChild(t);
        trails.push({ el: t, x: -100, y: -100 });
    }
    
    var mx = -100, my = -100;
    var hovered = false;

    window.addEventListener('mousemove', function(e) {
        mx = e.clientX; my = e.clientY;
        c.style.left = mx + 'px'; 
        c.style.top = my + 'px';
    });
    
    function loop() {
        var tx = mx, ty = my;
        for (var i = 0; i < numTrails; i++) {
            var tr = trails[i];
            tr.x += (tx - tr.x) * (0.3 - i * 0.02);
            tr.y += (ty - tr.y) * (0.3 - i * 0.02);
            tr.el.style.left = tr.x + 'px';
            tr.el.style.top = tr.y + 'px';
            tx = tr.x; ty = tr.y; // Next trail follows this one
            
            if (hovered) {
                tr.el.style.background = `rgba(56,189,248,${0.1 - i * 0.01})`;
                tr.el.style.transform = `translate(-50%,-50%) scale(1.5)`;
            } else {
                tr.el.style.background = 'transparent';
                tr.el.style.transform = `translate(-50%,-50%) scale(1)`;
            }
        }
        requestAnimationFrame(loop);
    }
    loop();
    
    function attach() {
        document.querySelectorAll('a, button, .qbtn, input, .wiz-btn, .premium-btn, .btn').forEach(function(el) {
            if (el.dataset.tc) return;
            el.dataset.tc = '1';
            el.addEventListener('mouseenter', () => hovered = true);
            el.addEventListener('mouseleave', () => hovered = false);
        });
    }
    attach(); setInterval(attach, 1500);
})();
