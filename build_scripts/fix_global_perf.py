import os

d = 'c:/projects/evolvix'
files = [f for f in os.listdir(d) if f.endswith('.html')]

target = """            (function tick(){
                var str='';
                for(var i=0;i<8;i++) str+=chars[Math.floor(Math.random()*chars.length)];
                stream.textContent=str+' // ACTIVE';
                requestAnimationFrame(tick);
            })();"""

replacement = """            (function tick(){
                var str='';
                for(var i=0;i<8;i++) str+=chars[Math.floor(Math.random()*chars.length)];
                stream.textContent=str+' // ACTIVE';
                setTimeout(tick, 80);
            })();"""

for f in files:
    path = os.path.join(d, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if target in content:
        content = content.replace(target, replacement)
        with open(path, 'w', encoding='utf-8') as file:
            f.write(content)
            
print("Done fixing HTML performance.")
