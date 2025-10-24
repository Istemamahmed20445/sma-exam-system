# 🚀 Complete Render Deployment Guide with Environment Variables

## Step-by-Step Instructions

### Step 1: Create Render Account (5 minutes)

1. Go to https://render.com
2. Click "Get Started" → "Sign Up"
3. Choose "Sign up with GitHub"
4. Authorize Render to access your GitHub account
5. Complete your profile

---

### Step 2: Create New Web Service (10 minutes)

1. **Click "New +" button** (top right)
2. **Select "Web Service"**
3. **Connect Repository:**
   - You'll see a list of your GitHub repositories
   - Find and click on `sma-exam-system`
   - Click "Connect"

---

### Step 3: Configure Settings

**Basic Settings:**

- **Name**: `sma-exam-system` (or your preferred name)
- **Region**: Choose closest to you (Singapore recommended for Asia)
- **Branch**: `main`
- **Root Directory**: (leave empty)
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Instance Type**: Free (to start)

**Click "Advanced" → Add these settings:**

- **Auto-Deploy**: Yes (auto-deploys on every push)

---

### Step 4: Add Environment Variables (CRITICAL!)

Scroll down to **"Environment Variables"** section and add these:

#### Required Variables:

**1. ADMIN_PASSWORD**
```
Key: ADMIN_PASSWORD
Value: [Your secure password - e.g., Admin@2024Secure!]
```
*This is your admin login password - make it strong!*

**2. FLASK_ENV**
```
Key: FLASK_ENV
Value: production
```

**3. FIREBASE_CONFIG** ⚠️ **MOST IMPORTANT**
```
Key: FIREBASE_CONFIG
Value: [Paste entire contents of firebase_config.json]
```

To get Firebase config:
1. Open `firebase_config.json` from your local project
2. Copy the ENTIRE file content
3. Paste it as the value for FIREBASE_CONFIG

Example format:
```json
{
  "type": "service_account",
  "project_id": "mock-exam-sma",
  "private_key_id": "...",
  "private_key": "...",
  "client_email": "...",
  "client_id": "...",
  "auth_uri": "...",
  "token_uri": "...",
  "auth_provider_x509_cert_url": "...",
  "client_x509_cert_url": "..."
}
```

---

### Step 5: Deployment

1. **Review all settings**
2. Click **"Create Web Service"**
3. **Wait for build** (5-10 minutes)
   - You'll see build logs in real-time
   - First deployment takes longer

---

### Step 6: After Deployment

Your app will be live at:
```
https://sma-exam-system.onrender.com
```

**Test it:**
1. Visit the URL
2. Test admin login
3. Create an exam
4. Test bulk upload
5. Share exam link with students

---

## 🔧 Troubleshooting

### Issue: "Application Error"

**Solution**: Check environment variables
1. Go to Render dashboard
2. Click your service
3. Go to "Environment" tab
4. Verify all variables are set correctly
5. Check logs for specific errors

### Issue: "Firebase Connection Failed"

**Solution**: 
1. Make sure FIREBASE_CONFIG is set correctly
2. Verify Firebase service account has proper permissions
3. Check Firebase console for errors

### Issue: "Module Not Found"

**Solution**:
1. Check `requirements.txt` has all dependencies
2. Look at build logs
3. May need to add missing packages

### Issue: "Build Failed"

**Solution**:
1. Check build logs
2. Verify Python version compatibility
3. Make sure all files are pushed to GitHub

---

## 📋 Environment Variables Quick Reference

### Required Variables:
```bash
ADMIN_PASSWORD=your-secure-password
FLASK_ENV=production
FIREBASE_CONFIG={"type":"service_account",...}
```

### How to Add in Render:
1. Dashboard → Your Service → Environment
2. Click "Add Environment Variable"
3. Enter Key and Value
4. Click "Save Changes"
5. Service will auto-restart

---

## 🎯 Post-Deployment Checklist

After deployment, verify:

- [ ] Homepage loads
- [ ] Admin login works
- [ ] Can create exams
- [ ] Can upload questions
- [ ] Bulk upload works
- [ ] Copy link works
- [ ] Students can take exams
- [ ] Results are saved
- [ ] Images upload correctly

---

## 💰 Render Pricing

**Free Tier:**
- ✅ 750 hours/month
- ✅ Enough for ~25 hours/day uptime
- ✅ Perfect for testing and small deployments

**Upgrade Later:**
- Starter: $7/month (more uptime)
- Professional: $25/month (dedicated resources)

---

## 🔄 Updating Your App

Any time you push to GitHub:

1. Make changes locally
2. Commit: `git add . && git commit -m "Update"`
3. Push: `git push origin main`
4. Render **automatically deploys** latest version!

---

## 📱 Your Live URLs

After deployment:

- **Homepage**: `https://sma-exam-system.onrender.com`
- **Admin**: `https://sma-exam-system.onrender.com/admin`
- **Student**: `https://sma-exam-system.onrender.com/`

---

## 🔐 Security Best Practices

✅ Use strong ADMIN_PASSWORD  
✅ Keep FIREBASE_CONFIG private  
✅ Don't commit secrets to GitHub  
✅ Use HTTPS (Render default)  
✅ Review logs regularly  

---

## 📞 Need Help?

- **Render Docs**: https://render.com/docs
- **Support**: Check Render dashboard logs
- **GitHub**: Check commit history

---

## 🎉 Success Indicators

You'll know deployment worked when:

✅ Build shows "Live" status  
✅ Visit URL shows your app  
✅ No errors in logs  
✅ Admin login works  
✅ All features functional  

---

**Ready to deploy? Follow steps 1-6 above!** 🚀

---

**Your Repository**: https://github.com/Istemamahmed20445/sma-exam-system  
**Quick Deploy**: See `QUICK_DEPLOY.md`  
**Last Updated**: October 24, 2025

