# ⚡ Quick Deploy Guide

## 🎯 What You Need
- GitHub account
- Render account
- 15 minutes

---

## 📝 Quick Steps

### 1️⃣ Push to GitHub (5 min)
```bash
# Create repo on GitHub first: https://github.com/new
# Then run:

git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

### 2️⃣ Deploy to Render (10 min)
1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect GitHub repo
4. Settings:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
5. Add Environment Variables:
   - `ADMIN_PASSWORD` = your password
   - `FIREBASE_CONFIG` = paste firebase_config.json content
6. Click "Create Web Service"
7. Wait 5-10 minutes

### 3️⃣ Done! ✅
Your app is live at: `https://your-app.onrender.com`

---

## 🔄 Adding Features Later

```bash
# 1. Make changes
# 2. Commit
git add .
git commit -m "New feature"
git push origin main

# 3. Render auto-deploys!
```

---

## 📚 Full Guide
See `DEPLOY_TO_RENDER.md` for detailed instructions.

---

**Ready? Let's deploy!** 🚀

