const fs = require("fs");

// 1. Fix index.html removals
let html = fs.readFileSync("index.html", "utf8");

// Remove EEAT author span
const eeatStart = html.indexOf('<span class="eeat-author-meta"');
if (eeatStart !== -1) {
    const eeatEnd = html.indexOf('</span>', eeatStart) + 7;
    // Wait, there are nested spans. The very last </span> is at the end of the line.
    const fullLineEnd = html.indexOf('\n', eeatStart);
    if (fullLineEnd !== -1) {
        html = html.substring(0, eeatStart) + html.substring(fullLineEnd);
    }
}

// Remove footer address block
const addressStart = html.indexOf('<address style="margin-top:1.5rem;font-size:.82rem;color:var(--text-secondary);line-height:1.9;font-style:normal;">');
if (addressStart !== -1) {
    const addressEnd = html.indexOf('</address>', addressStart) + 10;
    html = html.substring(0, addressStart) + html.substring(addressEnd);
}

fs.writeFileSync("index.html", html, "utf8");

// 2. Fix theme.js lag
let jsContent = fs.readFileSync("theme.js", "utf8");
jsContent = jsContent.replace("const particlesCount = 700;", "const particlesCount = 150;");
// Reduce pixel ratio for much better performance on high DPI screens
jsContent = jsContent.replace("renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));", "renderer.setPixelRatio(1);");

fs.writeFileSync("theme.js", jsContent, "utf8");

console.log("Removals and performance optimizations complete.");
