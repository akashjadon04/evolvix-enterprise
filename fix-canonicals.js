const fs = require("fs");
const path = require("path");

const dir = "c:/projects/evolvix";
const files = fs.readdirSync(dir).filter(f => f.endsWith(".html"));

files.forEach(file => {
    let content = fs.readFileSync(path.join(dir, file), "utf8");
    
    // 1. Remove all existing canonical tags using regex
    const canonicalRegex = /<link[^>]*rel=["']canonical["'][^>]*>/gi;
    const canonicalRegex2 = /<link[^>]*href=[^>]*rel=["']canonical["'][^>]*>/gi; // just in case
    
    content = content.replace(canonicalRegex, "");
    content = content.replace(canonicalRegex2, "");
    
    // 2. Generate correct canonical URL
    let slug = file.replace(".html", "");
    if (slug === "index" || slug === "index_old") slug = "";
    const canonicalUrl = `https://evolnex.digital${slug ? "/" + slug : "/"}`;
    
    // 3. Insert new canonical tag before </head>
    const canonicalTag = `\n  <link rel="canonical" href="${canonicalUrl}" />\n`;
    content = content.replace("</head>", `${canonicalTag}</head>`);
    
    fs.writeFileSync(path.join(dir, file), content, "utf8");
    console.log(`Updated canonical for ${file}: ${canonicalUrl}`);
});
