# 🎨 How to Add Your Company Logo

## Logo Requirements

To add your company logo, you need to:

1. **Create a logo file** (PNG format recommended)
2. **Name it**: `logo.png`
3. **Place it in**: `static/images/logo.png`
4. **Recommended size**: 80x80 pixels to 150x150 pixels
5. **Background**: Transparent PNG works best

---

## Steps to Add Logo

### 1. Prepare Your Logo
- Use a square logo or icon
- Size: 80x80 to 150x150 pixels
- Format: PNG with transparent background
- File size: Under 100KB for fast loading

### 2. Add Logo File
```bash
# Place your logo file here:
static/images/logo.png
```

### 3. Test
1. Refresh your browser
2. Logo will appear:
   - In browser tab (favicon)
   - In page header banners
   - On all pages (home, exam, results, admin)

---

## Logo Will Appear

✅ **Browser Tab** (favicon)
✅ **Home Page Header** - Left side of banner
✅ **Results Page Header** - Left side of banner  
✅ **Admin Login Header** - Left side of banner
✅ **All Pages** - Consistent branding

---

## What I've Already Done

✅ Added favicon link to all pages
✅ Added logo image to headers
✅ Created responsive CSS for logo display
✅ Configured logo for all templates

---

## Example Logo Path

```
Mock 3.0/
└── static/
    └── images/
        └── logo.png  ← Put your logo here
```

---

## Quick Test

1. Add a temporary logo file named `logo.png` to `static/images/`
2. Refresh browser
3. See logo in browser tab and headers
4. Replace with your actual logo when ready

---

## Need Help?

- Logo not showing? Check file path is correct
- Logo too big/small? Adjust size in CSS at `.logo` class
- Want different positioning? Edit `header-content` styles

---

## Current CSS

The logo is styled with:
```css
.logo {
    height: 80px;
    width: auto;
    object-fit: contain;
}
```

You can adjust the `height` value to make it bigger or smaller.

