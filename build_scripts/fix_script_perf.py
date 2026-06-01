import re

js_path = 'c:/projects/evolvix/script.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace PhysicsWorld instantiation with nothing
js = js.replace('if(window.innerWidth>768){(new PhysicsWorld).render()}else{setTimeout(()=>{if(window.innerWidth<=768){(new PhysicsWorld).render()}},3000)}', '')

# Replace MagneticButton instantiation with nothing
js = js.replace('document.querySelectorAll(".btn").forEach(t=>new MagneticButton(t)),', '')

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
