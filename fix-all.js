const fs = require("fs");
const files = ["index.html", "services.html", "about.html", "contact.html", "careers.html", "pricing.html", "case-studies.html"];

files.forEach(file => {
    if (fs.existsSync(file)) {
        let content = fs.readFileSync(file, "utf8");
        let changed = false;

        // Fix SyntaxError in gtag
        const badGtag = "function gtag(){dataLayer.push(arguments);--c-brand-main-rgb:14,116,144;--c-brand-light-rgb:103,232,249;}";
        const goodGtag = "function gtag(){dataLayer.push(arguments);}";
        if (content.includes(badGtag)) {
            content = content.replace(badGtag, goodGtag);
            changed = true;
        }

        // Fix canvas z-index issue
        const badCanvas = '<canvas id="webgl-hero" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1; pointer-events:none;"></canvas>';
        const goodCanvas = '<canvas id="webgl-hero" aria-hidden="true" style="position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;pointer-events:none;"></canvas>';
        if (content.includes(badCanvas)) {
            content = content.replace(badCanvas, goodCanvas);
            changed = true;
        }
        
        // Try alternate canvas
        const badCanvas2 = '<canvas id="webgl-hero" aria-hidden="true" style="position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:-1;pointer-events:none;"></canvas>';
        if (content.includes(badCanvas2)) {
            content = content.replace(badCanvas2, goodCanvas);
            changed = true;
        }

        if (changed) {
            fs.writeFileSync(file, content, "utf8");
            console.log("Fixed: " + file);
        }
    }
});
