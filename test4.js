const puppeteer = require("puppeteer");
(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto("file:///c:/projects/evolvix/services.html");
    await new Promise(r => setTimeout(r, 2000));
    
    // Check if preloader is visible
    const preloaderVisible = await page.evaluate(() => {
        const p = document.getElementById("preloader");
        return p ? window.getComputedStyle(p).opacity : "null";
    });
    
    // Check body height
    const bodyHeight = await page.evaluate(() => document.body.scrollHeight);
    
    console.log("Preloader opacity:", preloaderVisible);
    console.log("Body height:", bodyHeight);
    
    await browser.close();
})();
