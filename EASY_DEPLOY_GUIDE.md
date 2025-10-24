# 🚀 EASY Render Deployment Guide

## Follow These Simple Steps

---

## Step 1: Go to Render (2 minutes)

1. Open: https://render.com
2. Click "Get Started"
3. Click "Sign up with GitHub"
4. Allow Render to access your GitHub

---

## Step 2: Create Web Service (5 minutes)

1. Click **"New +"** button (top right)
2. Click **"Web Service"**
3. Find **"sma-exam-system"** in the list
4. Click **"Connect"**

---

## Step 3: Fill These Settings (5 minutes)

### Settings to Fill:

**Name**: `sma-exam-system`  
**Build Command**: `pip install -r requirements.txt`  
**Start Command**: `gunicorn app:app`  
**Plan**: Free  

*Leave everything else as default!*

---

## Step 4: Add Environment Variables (10 minutes)

Click **"Add Environment Variable"** button and add these THREE:

### Variable 1:
```
Key: ADMIN_PASSWORD
Value: Admin123Secure!
```

### Variable 2:
```
Key: FLASK_ENV
Value: production
```

### Variable 3 (Important!):
```
Key: FIREBASE_CONFIG
Value: [Paste everything from firebase_config.json file]
```

**To get Firebase config:**
1. Open `firebase_config.json` file on your computer
2. Copy EVERYTHING inside
3. Paste it as the Value

---

## Step 5: Deploy! (Wait 10 minutes)

1. Click **"Create Web Service"**
2. Watch the build logs
3. Wait for it to finish
4. Your app will be live!

---

## Your Live URL Will Be:

```
https://sma-exam-system.onrender.com
```

---

## That's It! 🎉

Visit your URL and test it!

---

## Troubleshooting

**If something doesn't work:**
1. Check Render logs
2. Make sure all 3 environment variables are added
3. Make sure FIREBASE_CONFIG is pasted correctly

---

**Need Help?** Check the logs in Render dashboard!

