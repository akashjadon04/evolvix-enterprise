import re

html_path = 'c:/projects/evolnex/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Reset the template container to display:none
old_style = 'style="position: absolute; left: -9999px; top: 0; width: 850px; background: #ffffff; font-family: \'Inter\', sans-serif;"'
new_style = 'style="display: none; width: 850px; background: #ffffff; font-family: \'Inter\', sans-serif;"'
html = html.replace(old_style, new_style)

# 2. Fix the JS generation logic to use a detached DOM node
js_to_replace = """    var element = document.getElementById('god-pdf-template');
    
    var opt = {
      margin:       0,
      filename:     'Evolnex_Strategy_Audit_' + name.replace(/[^a-z0-9]/gi, '_').toLowerCase() + '.pdf',
      image:        { type: 'jpeg', quality: 1.0 },
      html2canvas:  { scale: 2, useCORS: true, logging: false },
      jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
    };
    
    // Render
    html2pdf().set(opt).from(element).save().then(function() {
    });"""

# Because we removed element.style.display in the previous step, the current script looks like:
# var element = document.getElementById('god-pdf-template');
# var opt = ...
# html2pdf().set(opt).from(element).save().then(...)

new_js = """    // Create a completely detached element for html2pdf to prevent any offscreen/display:none bugs
    var pdfContainer = document.createElement('div');
    pdfContainer.style.width = '850px';
    pdfContainer.style.background = '#ffffff';
    pdfContainer.style.fontFamily = "'Inter', sans-serif";
    // Copy the inner HTML of our template
    pdfContainer.innerHTML = document.getElementById('god-pdf-template').innerHTML;
    
    var opt = {
      margin:       0,
      filename:     'Evolnex_Strategy_Audit_' + name.replace(/[^a-z0-9]/gi, '_').toLowerCase() + '.pdf',
      image:        { type: 'jpeg', quality: 1.0 },
      html2canvas:  { scale: 2, useCORS: true, letterRendering: true },
      jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
    };
    
    // Render from the detached element
    html2pdf().set(opt).from(pdfContainer).save();"""

# We can just regex replace the rendering block
html = re.sub(r'var element = document\.getElementById\(\'god-pdf-template\'\);.*?\}\);', new_js, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
