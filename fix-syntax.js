const fs = require("fs");
let theme = fs.readFileSync("theme.js", "utf8");

const rogueBlock = `    } else if (heroCanvas) {
        // Hide canvas on mobile or if Three.js not loaded
        heroCanvas.style.display = 'none';
    }`;

if (theme.includes(rogueBlock)) {
    theme = theme.replace(rogueBlock, "    }");
    fs.writeFileSync("theme.js", theme, "utf8");
    console.log("Syntax error fixed successfully");
} else {
    console.log("Rogue block not found");
}
