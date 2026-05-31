"use strict";const MathUtils={lerp:(t,e,s)=>t*(1-s)+e*s,clamp:(t,e,s)=>Math.min(Math.max(t,e),s),map:(t,e,s,i,n)=>(t-e)/(s-e)*(n-i)+i,dist:(t,e,s,i)=>Math.hypot(s-t,i-e),rand:(t,e)=>Math.random()*(e-t)+t};class Vector2{constructor(t=0,e=0){this.x=t,this.y=e}add(t){return this.x+=t.x,this.y+=t.y,this}sub(t){return this.x-=t.x,this.y-=t.y,this}mult(t){return this.x*=t,this.y*=t,this}div(t){return this.x/=t,this.y/=t,this}mag(){return Math.sqrt(this.x*this.x+this.y*this.y)}normalize(){let t=this.mag();return 0!==t&&this.div(t),this}limit(t){return this.mag()>t&&(this.normalize(),this.mult(t)),this}copy(){return new Vector2(this.x,this.y)}static sub(t,e){return new Vector2(t.x-e.x,t.y-e.y)}}class Particle{constructor(t,e){this.pos=new Vector2(Math.random()*t,Math.random()*e),this.vel=new Vector2(2*Math.random()-1,2*Math.random()-1),this.acc=new Vector2(0,0),this.size=3*Math.random()+1,this.maxSpeed=2,this.maxForce=.05,this.baseColor=`rgba(14, 116, 144, ${.5*Math.random()+.1})`}applyForce(t){this.acc.add(t)}update(t,e){this.vel.add(this.acc),this.vel.limit(this.maxSpeed),this.pos.add(this.vel),this.acc.mult(0),this.pos.x>t&&(this.pos.x=0),this.pos.x<0&&(this.pos.x=t),this.pos.y>e&&(this.pos.y=0),this.pos.y<0&&(this.pos.y=e)}draw(t){t.beginPath(),t.arc(this.pos.x,this.pos.y,this.size,0,2*Math.PI),t.fillStyle=this.baseColor,t.fill()}behaviors(t){let e=Vector2.sub(this.pos,t),s=e.mag();if(s>120||s<1)return;let i=MathUtils.map(s,0,120,.015,0);e.normalize(),e.mult(i),this.applyForce(e)}}class PhysicsWorld{constructor(){this.canvas=document.createElement("canvas"),this.canvas.id="physics-bg",this.canvas.style.position="fixed",this.canvas.style.top="0",this.canvas.style.left="0",this.canvas.style.width="100%",this.canvas.style.height="100%",this.canvas.style.zIndex="-1",this.canvas.style.pointerEvents="none",document.body.appendChild(this.canvas),this.ctx=this.canvas.getContext("2d"),this.particles=[],this.mouse=new Vector2(-100,-100),this.particleCount=window.innerWidth<768?8:15,this.resize(),this.initParticles(),window.addEventListener("resize",()=>this.resize()),window.addEventListener("mousemove",t=>{this.mouse.x=t.clientX,this.mouse.y=t.clientY})}resize(){this.width=window.innerWidth,this.height=window.innerHeight,this.canvas.width=this.width,this.canvas.height=this.height}initParticles(){this.particles=[];for(let t=0;t<this.particleCount;t++)this.particles.push(new Particle(this.width,this.height))}render(){this.ctx.clearRect(0,0,this.width,this.height);for(let t=0;t<this.particles.length;t++){let e=this.particles[t];e.behaviors(this.mouse),e.update(this.width,this.height),e.draw(this.ctx);}requestAnimationFrame(()=>this.render())}}class MagneticButton{constructor(t){this.el=t,this.rect=null,this.text=this.el.innerText,this.centerX=0,this.centerY=0,this.mouse={x:0,y:0},this.pos={x:0,y:0},this.isHovering=!1,this.init()}init(){this.el.addEventListener("mouseenter",()=>this.updateRect()),this.el.addEventListener("mousemove",t=>this.onMove(t)),this.el.addEventListener("mouseleave",()=>this.onLeave()),this.loop()}updateRect(){this.rect=this.el.getBoundingClientRect(),this.centerX=this.rect.left+this.rect.width/2,this.centerY=this.rect.top+this.rect.height/2}onMove(t){this.isHovering=!0,this.mouse.x=t.clientX,this.mouse.y=t.clientY}onLeave(){this.isHovering=!1}loop(){let t=0,e=0;if(this.isHovering&&this.rect){t=.4*(this.mouse.x-this.centerX),e=.4*(this.mouse.y-this.centerY)}this.pos.x=MathUtils.lerp(this.pos.x,t,.1),this.pos.y=MathUtils.lerp(this.pos.y,e,.1),this.el.style.transform=`translate(${this.pos.x}px, ${this.pos.y}px)`,requestAnimationFrame(()=>this.loop())}}class SmoothScroll{constructor(){this.target=0,this.current=0,this.ease=.08,this.windowHeight=window.innerHeight,this.prefersReducedMotion=window.matchMedia("(prefers-reduced-motion: reduce)").matches,this.prefersReducedMotion||(document.body.style.height=`${document.documentElement.scrollHeight}px`,this.container=document.querySelector("main"),this.container&&(this.container.style.position="fixed",this.container.style.top=0,this.container.style.left=0,this.container.style.width="100%",this.loop())),window.addEventListener("scroll",()=>{this.target=window.scrollY}),window.addEventListener("resize",()=>{document.body.style.height=`${document.documentElement.scrollHeight}px`})}loop(){this.current=MathUtils.lerp(this.current,this.target,this.ease),this.container&&(this.container.style.transform=`translate3d(0, -${this.current}px, 0)`),requestAnimationFrame(()=>this.loop())}}class AuditFormPhysics{constructor(){this.form=document.getElementById("audit-form"),this.input=document.getElementById("audit-url"),this.btn=document.getElementById("audit-submit"),this.form&&this.init()}init(){this.btn.addEventListener("click",t=>{this.input.value.includes(".")?this.explodeSuccess(t):(t.preventDefault(),this.shakeForm())}),this.input.addEventListener("focus",()=>{this.form.style.transform="scale(1.02)",this.form.style.boxShadow="0 20px 40px rgba(14, 116, 144, 0.2)"}),this.input.addEventListener("blur",()=>{this.form.style.transform="scale(1)",this.form.style.boxShadow="none"})}shakeForm(){this.form.animate([{transform:"translateX(0)"},{transform:"translateX(-10px)"},{transform:"translateX(10px)"},{transform:"translateX(-10px)"},{transform:"translateX(0)"}],{duration:300}),this.input.style.borderColor="#ef4444"}explodeSuccess(t){const e=this.btn.getBoundingClientRect();for(let t=0;t<30;t++)this.createConfetti(e.left+e.width/2,e.top+e.height/2)}createConfetti(t,e){const s=document.createElement("div");s.style.position="fixed",s.style.left=t+"px",s.style.top=e+"px",s.style.width="8px",s.style.height="8px",s.style.background=`hsl(${360*Math.random()}, 100%, 50%)`,s.style.borderRadius="50%",s.style.pointerEvents="none",s.style.zIndex="9999",document.body.appendChild(s);const i=300*(Math.random()-.5),n=300*(Math.random()-.5);s.animate([{transform:"translate(0,0) scale(1)",opacity:1},{transform:`translate(${i}px, ${n}px) scale(0)`,opacity:0}],{duration:1e3,easing:"cubic-bezier(0, .9, .57, 1)"}).onfinish=()=>s.remove()}}class CardTilt{constructor(t){this.el=t,this._r=null,this._w=0,this._h=0,this.el.addEventListener("mouseenter",()=>{this._r=this.el.getBoundingClientRect();this._w=this._r.width;this._h=this._r.height}),this.el.addEventListener("mousemove",t=>this.handleMove(t)),this.el.addEventListener("mouseleave",()=>this.handleLeave())}handleMove(t){if(!this._r)return;const e=this._h,s=this._w,i=this._r,r=t.clientX-i.left,h=t.clientY-i.top,o=`perspective(1000px) scale(1.05) rotateX(${(h-e/2)/e*-20}deg) rotateY(${(r-s/2)/s*20}deg)`;this.el.style.transform=o;this.el.style.setProperty("--mouse-x",`${r}px`),this.el.style.setProperty("--mouse-y",`${h}px`)}handleLeave(){this.el.style.transform="perspective(1000px) scale(1) rotateX(0) rotateY(0)";this._r=null}}class PageLoader{constructor(){this.links=document.querySelectorAll("a"),this.overlay=document.createElement("div"),this.overlay.style.cssText="\n            position: fixed; top: 0; left: 0; width: 100%; height: 100%;\n            background: #000; z-index: 99999; transform: scaleY(0);\n            transform-origin: bottom; transition: transform 0.6s cubic-bezier(0.87, 0, 0.13, 1);\n        ",document.body.appendChild(this.overlay),this.init()}init(){window.addEventListener("pageshow",()=>{this.overlay.style.transformOrigin="top",this.overlay.style.transform="scaleY(0)"}),this.links.forEach(t=>{t.hostname===window.location.hostname&&-1===t.getAttribute("href").indexOf("#")&&t.addEventListener("click",e=>{e.preventDefault();const s=t.getAttribute("href");this.transitionTo(s)})})}transitionTo(t){this.overlay.style.transformOrigin="bottom",this.overlay.style.transform="scaleY(1)",setTimeout(()=>{window.location.href=t},600)}}document.addEventListener("DOMContentLoaded",()=>{(new PhysicsWorld).render(),document.querySelectorAll(".btn").forEach(t=>new MagneticButton(t)),document.querySelectorAll(".card, .glass-card").forEach(t=>new CardTilt(t));new AuditFormPhysics,new PageLoader;window.innerWidth;const t=new IntersectionObserver(t=>{t.forEach(t=>{if(t.isIntersecting){t.target.classList.add("active");t.target.querySelectorAll(".stagger-child").forEach((t,e)=>{setTimeout(()=>{t.classList.add("visible")},100*e)})}})},{threshold:.1});document.querySelectorAll(".reveal").forEach(e=>t.observe(e));const e=document.querySelector(".nav-toggle"),s=document.querySelector(".nav-menu");e&&s&&(e.addEventListener("click",()=>{s.classList.toggle("active"),e.classList.toggle("active"),s.classList.contains("active")?e.innerHTML="✕":e.innerHTML="☰"}),document.querySelectorAll(".nav-link").forEach(t=>{t.addEventListener("click",()=>{s.classList.remove("active"),e.innerHTML="☰"})})),console.log("SUMMITFORGE V6: GOD MODE ENGINE ACTIVE")});




/* ─── Premium Magnetic Trailing Cursor ─── */
(function(){
    if(!window.matchMedia('(pointer:fine)').matches) return; // Only desktop
    
    // Main cursor dot
    var c=document.createElement('div');
    c.style.cssText='position:fixed;top:0;left:0;width:8px;height:8px;background:#38bdf8;border-radius:50%;pointer-events:none;z-index:999999;transform:translate(-50%,-50%);transition:transform 0.1s;';
    document.body.appendChild(c);

    // Trail elements
    var trails = [];
    var numTrails = 6;
    for(var i=0; i<numTrails; i++) {
        var t = document.createElement('div');
        t.style.cssText=`position:fixed;top:0;left:0;width:${24 - i*3}px;height:${24 - i*3}px;border:1px solid rgba(56,189,248,${0.6 - i*0.1});border-radius:50%;pointer-events:none;z-index:${999998-i};transform:translate(-50%,-50%);`;
        document.body.appendChild(t);
        trails.push({el: t, x: -100, y: -100});
    }
    
    var mx=-100, my=-100;
    var hovered = false;

    window.addEventListener('mousemove', function(e){
        mx = e.clientX; my = e.clientY;
        c.style.left = mx+'px'; 
        c.style.top = my+'px';
    });
    
    function loop(){
        var tx = mx, ty = my;
        for(var i=0; i<numTrails; i++){
            var tr = trails[i];
            tr.x += (tx - tr.x) * (0.3 - i*0.02);
            tr.y += (ty - tr.y) * (0.3 - i*0.02);
            tr.el.style.left = tr.x + 'px';
            tr.el.style.top = tr.y + 'px';
            tx = tr.x; ty = tr.y; // Next trail follows this one
            
            if(hovered) {
                tr.el.style.background = `rgba(56,189,248,${0.1 - i*0.01})`;
                tr.el.style.transform = `translate(-50%,-50%) scale(1.5)`;
            } else {
                tr.el.style.background = 'transparent';
                tr.el.style.transform = `translate(-50%,-50%) scale(1)`;
            }
        }
        requestAnimationFrame(loop);
    }
    loop();
    
    function attach(){
        document.querySelectorAll('a, button, .qbtn, input, .wiz-btn, .premium-btn, .btn').forEach(function(el){
            if(el.dataset.tc) return;
            el.dataset.tc = '1';
            el.addEventListener('mouseenter', ()=>hovered=true);
            el.addEventListener('mouseleave', ()=>hovered=false);
        });
    }
    attach(); setInterval(attach, 1500);
})();
