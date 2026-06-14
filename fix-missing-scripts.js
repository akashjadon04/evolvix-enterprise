const fs = require("fs");
const files = ["services.html", "about.html", "contact.html", "careers.html", "pricing.html", "case-studies.html"];

files.forEach(file => {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, "utf8");
        
        // Let's find the broken exit-avatars part
        const brokenTarget = `<span style="background:linear-gradient(135deg,#8b5cf6,#c084fc)">R</span>
        var bar=document.getElementById('preloaderBar')`;
        
        const goodReplacement = `<span style="background:linear-gradient(135deg,#8b5cf6,#c084fc)">R</span>
  </div>
  <span>Join 500+ founders</span>
  </div>
  </div>
  <script>
      (function(){
        var bar=document.getElementById('preloaderBar')`;
        
        if (content.includes(brokenTarget)) {
            content = content.replace(brokenTarget, goodReplacement);
            fs.writeFileSync(file, content, "utf8");
            console.log("Fixed missing script tag in: " + file);
        } else {
            // Alternative match if whitespace differs
            const regex = /<span style="background:linear-gradient\(135deg,#8b5cf6,#c084fc\)">R<\/span>[\s\r\n]*var bar=document\.getElementById\('preloaderBar'\)/;
            if (regex.test(content)) {
                content = content.replace(regex, `<span style="background:linear-gradient(135deg,#8b5cf6,#c084fc)">R</span>\n  </div>\n  <span>Join 500+ founders</span>\n  </div>\n  </div>\n  <script>\n      (function(){\n        var bar=document.getElementById('preloaderBar')`);
                fs.writeFileSync(file, content, "utf8");
                console.log("Fixed missing script tag in (regex): " + file);
            }
        }
    }
});
