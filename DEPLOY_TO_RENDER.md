# 🚀 Deploy to GitHub & Render - Complete Guide

## Prerequisites
- GitHub account
- Render account (free tier available)
- Firebase credentials ready

---

## Step 1: Push to GitHub

### 1.1 Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `shahriar-medical-academy-mock-exam`
3. Set to **Private** (recommended for production)
4. Click "Create repository"

### 1.2 Push Your Code
```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/shahriar-medical-academy-mock-exam.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy to Render

### 2.1 Create Render Account
1. Go to https://render.com
2. Sign up with GitHub
3. Connect your GitHub account

### 2.2 Create New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Find `shahriar-medical-academy-mock-exam`
4. Click "Connect"

### 2.3 Configure Deployment
**Settings:**
- **Name**: `shahriar-medical-academy-mock-exam`
- **Region**: Singapore (or closest to you)
- **Branch**: `main`
- **Root Directory**: (leave empty)
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: Free (to start)

### 2.4 Add Environment Variables
Click "Environment" tab and add:

```
ADMIN_PASSWORD=your-secure-password-here
FLASK_ENV=production
```

**Important**: Generate a strong password for ADMIN_PASSWORD!

### 2.5 Add Firebase Credentials
In Render dashboard:
1. Go to "Environment" section
2. Click "Add Environment Variable"
3. Name: `FIREBASE_CONFIG`
4. Value: Paste the entire contents of your `firebase_config.json` file

**Format:**
```json
{
  "type": "service_account",
  "project_id": "mock-exam-sma",
  ...
}
```

### 2.6 Deploy
1. Click "Create Web Service"
2. Wait for build to complete (5-10 minutes)
3. Your app will be live at: `https://shahriar-medical-academy-mock-exam.onrender.com`

---

## Step 3: Verify Deployment

### 3.1 Test Your Site
1. Visit your Render URL
2. Check homepage loads
3. Test admin login
4. Test creating an exam
5. Test bulk upload

### 3.2 Common Issues

**Issue: "Application Error"**
- Check environment variables are set
- Verify Firebase credentials
- Check build logs in Render dashboard

**Issue: "Module Not Found"**
- Make sure `requirements.txt` has all dependencies
- Check build logs for errors

**Issue: "Firebase Connection Failed"**
- Verify FIREBASE_CONFIG environment variable
- Check Firebase service account permissions

---

## Step 4: Set Up Automatic Deployments

### 4.1 Render Auto-Deploy
✅ Already configured!
- Push to `main` branch = automatic deployment
- New builds trigger automatically

### 4.2 Manual Deploy
If you need to manually deploy:
1. Go to Render dashboard
2. Click "Manual Deploy"
3. Select "Deploy latest commit"

---

## Step 5: Future Development Workflow

### Adding New Features
```bash
# 1. Create a new branch
git checkout -b feature/new-feature-name

# 2. Make your changes
# ... edit files ...

# 3. Commit changes
git add .
git commit -m "Add new feature"

# 4. Push to GitHub
git push origin feature/new-feature-name

# 5. Create Pull Request on GitHub
# 6. Merge to main
# 7. Render auto-deploys!
```

### Updating Production
```bash
# Make changes locally
git add .
git commit -m "Fix bug or add feature"
git push origin main

# Render automatically deploys latest version
```

---

## Important Files

### `render.yaml`
- Deployment configuration
- Environment variables
- Build commands

### `.gitignore`
- Prevents uploading secrets
- Firebase credentials excluded
- Python cache files excluded

### `requirements.txt`
- Python dependencies
- Version pinned for stability

---

## Security Checklist

✅ Firebase credentials NOT in GitHub (in .gitignore)  
✅ Admin password as environment variable  
✅ Production environment set  
✅ HTTPS enabled (Render default)  
✅ Strong password for admin access  

---

## Cost Estimate

**Render Free Tier:**
- ✅ 750 hours/month free
- ✅ Enough for ~25 hours/day uptime
- ✅ Perfect for testing and small deployments

**If You Need More:**
- Starter Plan: $7/month (more uptime)
- Professional: $25/month (dedicated resources)

---

## Useful Commands

### Local Development
```bash
# Start local server
source venv/bin/activate
python app.py

# Access at: http://localhost:5001
```

### Git Commands
```bash
# Check status
git status

# View commits
git log

# Update from GitHub
git pull origin main

# Push changes
git push origin main
```

---

## Rollback if Needed

### On Render
1. Go to "Deploys" tab
2. Find previous successful deploy
3. Click "..." → "Redeploy this commit"

### On GitHub
```bash
# View git tags
git tag

# Rollback to previous version
git checkout sma-mock1
git push origin sma-mock1 --force
```

---

## Support Resources

- **Render Docs**: https://render.com/docs
- **GitHub Docs**: https://docs.github.com
- **Flask Docs**: https://flask.palletsprojects.com
- **Firebase Docs**: https://firebase.google.com/docs

---

## Next Steps

1. ✅ Push to GitHub
2. ✅ Deploy to Render
3. ✅ Test production site
4. ✅ Share link with students
5. 🎉 Add more features as needed!

---

**Ready to deploy? Follow the steps above!** 🚀

---

**Last Updated**: October 24, 2025  
**Version**: SMA Mock 1.0  
**Tag**: sma-mock1

