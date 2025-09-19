# Visual Asset Generation System - PNG Ready

## Brand Guidelines for Visual Assets

### Color Palette
```css
:root {
  --brand-navy: #1a365d;
  --brand-gray: #2d3748;
  --brand-blue: #4299e1;
  --brand-gold: #f6ad55;
  --text-white: #ffffff;
  --text-light: rgba(255, 255, 255, 0.9);
}
```

### Typography
- **Primary Font**: Inter, Arial, sans-serif
- **Quote Font**: Georgia, serif (for elegance)
- **Sizes**: 
  - Main Quote: 24-28px
  - Attribution: 14px
  - Stats: 48px (numbers), 18px (description)

## PNG Asset Templates

### 1. Quote Card Template (1080x1080px)
```html
<div class="quote-card" style="
  width: 1080px; 
  height: 1080px; 
  background: linear-gradient(135deg, #1a365d, #4299e1);
  padding: 80px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: white;
  font-family: 'Inter', sans-serif;
">
  <div style="font-size: 64px; font-weight: 300; margin-bottom: 40px; opacity: 0.8;">"</div>
  
  <h2 style="
    font-size: 28px; 
    font-weight: 600; 
    line-height: 1.4; 
    margin-bottom: 60px;
    text-align: left;
  ">
    AI doesn't replace humans. It replaces tasks.
  </h2>
  
  <div style="
    font-size: 14px; 
    opacity: 0.9;
    border-top: 1px solid rgba(255,255,255,0.3);
    padding-top: 20px;
  ">
    Frank X, Oracle AI Center of Excellence
  </div>
</div>
```

### 2. Statistics Card Template (1080x1080px)
```html
<div class="stats-card" style="
  width: 1080px; 
  height: 1080px; 
  background: linear-gradient(135deg, #f6ad55, #ed8936);
  padding: 80px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: white;
  font-family: 'Inter', sans-serif;
">
  <div style="
    font-size: 120px; 
    font-weight: 800; 
    line-height: 0.9;
    margin-bottom: 30px;
  ">
    97M
  </div>
  
  <h3 style="
    font-size: 24px; 
    font-weight: 600; 
    margin-bottom: 20px;
    max-width: 600px;
  ">
    NEW jobs will be created by AI
  </h3>
  
  <p style="
    font-size: 18px; 
    opacity: 0.9;
    max-width: 500px;
  ">
    But 95% of people are training for the disappearing ones
  </p>
  
  <div style="
    font-size: 12px; 
    margin-top: 60px;
    opacity: 0.8;
    border-top: 1px solid rgba(255,255,255,0.3);
    padding-top: 20px;
  ">
    Source: World Economic Forum 2025 • Frank X Analysis
  </div>
</div>
```

### 3. Process Insight Card (1080x1350px - Instagram)
```html
<div class="process-card" style="
  width: 1080px; 
  height: 1350px; 
  background: linear-gradient(135deg, #2d3748, #1a202c);
  padding: 100px 80px;
  color: white;
  font-family: 'Inter', sans-serif;
">
  <div style="margin-bottom: 80px;">
    <h1 style="
      font-size: 32px; 
      font-weight: 700; 
      margin-bottom: 40px;
      text-align: center;
    ">
      The AI Skills Everyone's Learning Won't Save Your Job
    </h1>
  </div>
  
  <div style="space-y: 40px;">
    <div style="display: flex; align-items: center; margin-bottom: 40px;">
      <div style="
        background: #4299e1; 
        width: 40px; 
        height: 40px; 
        border-radius: 50%;
        margin-right: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
      ">1</div>
      <p style="font-size: 18px;">Creative Problem-Solving</p>
    </div>
    
    <div style="display: flex; align-items: center; margin-bottom: 40px;">
      <div style="
        background: #4299e1; 
        width: 40px; 
        height: 40px; 
        border-radius: 50%;
        margin-right: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
      ">2</div>
      <p style="font-size: 18px;">Emotional Intelligence</p>
    </div>
    
    <div style="display: flex; align-items: center; margin-bottom: 40px;">
      <div style="
        background: #4299e1; 
        width: 40px; 
        height: 40px; 
        border-radius: 50%;
        margin-right: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
      ">3</div>
      <p style="font-size: 18px;">Strategic Thinking</p>
    </div>
    
    <div style="display: flex; align-items: center; margin-bottom: 40px;">
      <div style="
        background: #4299e1; 
        width: 40px; 
        height: 40px; 
        border-radius: 50%;
        margin-right: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
      ">4</div>
      <p style="font-size: 18px;">Relationship Building</p>
    </div>
  </div>
  
  <div style="
    text-align: center; 
    margin-top: 80px;
    font-size: 14px;
    opacity: 0.8;
    border-top: 1px solid rgba(255,255,255,0.2);
    padding-top: 30px;
  ">
    Frank X • Oracle AI Center of Excellence
  </div>
</div>
```

## PNG Generation Instructions

### For Automated Generation (using tools like Puppeteer, Playwright, or Canvas API):

```javascript
// Example PNG generation script
const puppeteer = require('puppeteer');

async function generateQuoteCard(quote, author, cardType = 'navy') {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  await page.setViewport({ width: 1080, height: 1080 });
  
  const html = `
    <!DOCTYPE html>
    <html>
    <head>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    </head>
    <body style="margin: 0; padding: 0;">
      ${getCardHTML(quote, author, cardType)}
    </body>
    </html>
  `;
  
  await page.setContent(html);
  await page.screenshot({
    path: `quote-card-${Date.now()}.png`,
    fullPage: true,
    type: 'png'
  });
  
  await browser.close();
}
```

### Manual Creation Guidelines:
1. **Use Canva Templates**: Create brand-consistent templates in Canva
2. **Figma Components**: Build reusable card components
3. **Adobe Express**: Quick social media card generation
4. **PowerPoint/Keynote**: Simple template system for quick creation

## Asset Organization Structure

```
/visual-assets/
├── templates/
│   ├── quote-card-navy.html
│   ├── quote-card-gold.html
│   ├── stats-card.html
│   └── process-card.html
├── generated/
│   ├── YYYY-MM-DD/
│   │   ├── quote-card-1.png
│   │   ├── quote-card-2.png
│   │   └── stats-card.png
├── brand-assets/
│   ├── logo.png
│   ├── fonts/
│   └── color-palette.css
```

## Quick Generation Workflow

### Daily Asset Creation Process:
1. **Extract Key Quotes**: Identify 2-3 shareable quotes from content
2. **Identify Key Stats**: Find the most impactful statistic
3. **Generate Cards**: Use templates to create 3-4 visual assets
4. **Brand Check**: Ensure consistent colors, fonts, attribution
5. **Export**: Save as 1080x1080 PNG for optimal social media use

### Asset Naming Convention:
- `quote-card-YYYY-MM-DD-01.png`
- `stats-card-YYYY-MM-DD-01.png`
- `process-card-YYYY-MM-DD-01.png`

## Platform Specifications

### LinkedIn:
- **Recommended**: 1200x627px (link preview)
- **Square Posts**: 1080x1080px
- **Article Headers**: 1200x627px

### Twitter/X:
- **Standard**: 1200x675px (16:9)
- **Square**: 1080x1080px
- **Header**: 1500x500px

### Instagram:
- **Square**: 1080x1080px
- **Story**: 1080x1920px
- **Reel Cover**: 1080x1350px

This system ensures every piece of content has accompanying visual assets ready for immediate publishing across all platforms.