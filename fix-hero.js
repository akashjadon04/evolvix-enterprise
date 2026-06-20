const fs = require("fs");
const files = ["index.html", "services.html", "about.html", "contact.html", "careers.html", "pricing.html", "case-studies.html"];

files.forEach(file => {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, "utf8");
        const badHero = ".hero{min-height:100vh;display:flex;align-items:center;padding-top:90px";
        const goodHero = ".hero{position:relative;z-index:1;min-height:100vh;display:flex;align-items:center;padding-top:90px";
        
        if (content.includes(badHero)) {
            content = content.replace(badHero, goodHero);
            fs.writeFileSync(file, content, "utf8");
            console.log("Fixed hero z-index in: " + file);
        }
    }
});
