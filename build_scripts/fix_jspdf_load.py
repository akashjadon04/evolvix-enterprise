import os

d = 'c:/projects/evolnex'
files = [f for f in os.listdir(d) if f.endswith('.html')]

script_tag = '<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>'

for f in files:
    path = os.path.join(d, f)
    with open(path, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # We check if it is explicitly imported in the head
    # Or we can just insert it right before </head> if it's not already in the head block.
    
    head_end_idx = html.find('</head>')
    if head_end_idx != -1:
        head_block = html[:head_end_idx]
        if script_tag not in head_block:
            html = html.replace('</head>', script_tag + '\n</head>', 1)
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(html)
            print(f"Added jsPDF script to {f}")

print("Fixed jsPDF loading.")
