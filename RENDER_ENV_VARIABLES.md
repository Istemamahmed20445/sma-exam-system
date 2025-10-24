# 🔐 Environment Variables for Render Deployment

## 📋 Copy & Paste These 3 Variables

Add these in Render Dashboard → Your Service → Environment tab:

---

## ✅ Variable 1: ADMIN_PASSWORD

**Key:** `ADMIN_PASSWORD`  
**Value:** `Admin@2024Secure!`

*(Or use your own secure password)*

---

## ✅ Variable 2: FLASK_ENV

**Key:** `FLASK_ENV`  
**Value:** `production`

*(Must be exactly "production")*

---

## ✅ Variable 3: FIREBASE_CONFIG ⚠️ IMPORTANT

**Key:** `FIREBASE_CONFIG`  
**Value:** Copy and paste the ENTIRE content from your `firebase_config.json` file

**How to get it:**
1. Open the file `firebase_config.json` in your local project
2. Copy ALL the content (from `{` to `}`)
3. Paste it as the value for FIREBASE_CONFIG

**⚠️ IMPORTANT:** 
- Copy the ENTIRE JSON object (including all curly braces)
- Include all fields
- No extra spaces or characters

---

## 📝 How to Add Them in Render

1. Go to https://render.com/dashboard
2. Click on your service (sma-exam-system)
3. Click **"Environment"** tab (left sidebar)
4. Click **"Add Environment Variable"** button
5. Add each one separately:
   - Type the Key name (exactly as shown)
   - Paste the Value
   - Click **"Save Changes"**
6. Repeat for all 3 variables

---

## ⚠️ Important Notes

- The FIREBASE_CONFIG must be the ENTIRE JSON object
- Include all the text from `{` to `}`
- No extra spaces or characters
- After adding all 3 variables, your app will automatically redeploy

---

## ✅ That's It!

After adding these 3 variables, Render will automatically redeploy.

Your app will start working! 🎉

