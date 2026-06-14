const puppeteer = require("puppeteer");
(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 800 });
    await page.goto("file:///c:/projects/evolvix/services.html");
    await new Promise(r => setTimeout(r, 2000));
    await page.screenshot({ path: "debug_services.png" });
    await browser.close();
})();
