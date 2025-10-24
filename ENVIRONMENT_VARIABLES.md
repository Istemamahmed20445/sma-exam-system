# 🔐 Environment Variables Required for Render

## Complete List of Environment Variables

You need to add these **3 environment variables** in Render:

---

## 1. ADMIN_PASSWORD ⚠️ **REQUIRED**

**Purpose**: Admin login password

**Type**: String

**Example Value**:
```
Admin@2024Secure!
```

**How to Set**:
1. Go to Render Dashboard
2. Your Service → Environment tab
3. Add: `ADMIN_PASSWORD` = `[Your secure password]`

**Security Note**: Use a strong password with letters, numbers, and special characters!

---

## 2. FLASK_ENV ⚠️ **REQUIRED**

**Purpose**: Sets Flask to production mode

**Type**: String

**Exact Value**:
```
production
```

**How to Set**:
1. Environment tab in Render
2. Add: `FLASK_ENV` = `production`

**Why**: Disables debug mode and optimizes for production

---

## 3. FIREBASE_CONFIG ⚠️ **MOST CRITICAL**

**Purpose**: Firebase service account credentials

**Type**: JSON String

**Value**: Entire contents of `firebase_config.json` file

**How to Get**:
1. Open `firebase_config.json` from your local project
2. Copy ALL contents (from `{` to `}`)
3. Paste as value

**Example Format**:
```json
{
  "type": "service_account",
  "project_id": "mock-exam-sma",
  "private_key_id": "abc123...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-...@mock-exam-sma.iam.gserviceaccount.com",
  "client_id": "123456789",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/..."
}
```

**How to Set**:
1. Environment tab in Render
2. Click "Add Environment Variable"
3. Key: `FIREBASE_CONFIG`
4. Value: Paste entire JSON content
5. Click "Save Changes"

**Important**: 
- ✅ Copy the ENTIRE file content
- ✅ Include opening `{` and closing `}`
- ✅ Keep all line breaks (`\n`) intact
- ✅ This is required for Firebase connection!

---

## Summary Table

| Variable | Value Type | Required | Description |
|----------|-----------|----------|-------------|
| `ADMIN_PASSWORD` | String | ✅ Yes | Your admin login password |
| `FLASK_ENV` | String | ✅ Yes | Set to `production` |
| `FIREBASE_CONFIG` | JSON | ✅ Yes | Firebase credentials |

---

## How to Add in Render

### Step-by-Step:

1. **Go to Render Dashboard**
   - https://render.com/dashboard

2. **Click Your Service**
   - Find `sma-exam-system` service

3. **Go to "Environment" Tab**
   - Left sidebar → Environment

4. **Add Each Variable**:
   - Click "Add Environment Variable"
   - Enter Key
   - Enter Value
   - Click "Save Changes"

5. **Service Auto-Restarts**
   - Render will restart your service
   - Wait 1-2 minutes

---

## Example Setup in Render

```
Environment Variables:
───────────────────────
Key: ADMIN_PASSWORD
Value: Admin@2024Secure!

Key: FLASK_ENV
Value: production

Key: FIREBASE_CONFIG
Value: {"type":"service_account","project_id":"mock-exam-sma",...}
```

---

## Troubleshooting

### "Application Error" After Adding Variables

**Solution**:
1. Check FIREBASE_CONFIG is valid JSON
2. Verify ADMIN_PASSWORD is set
3. Check service logs for specific errors

### "Firebase Connection Failed"

**Solution**:
1. Re-check FIREBASE_CONFIG value
2. Make sure entire JSON is copied
3. No extra spaces before/after JSON
4. Verify Firebase service account permissions

### "Admin Login Doesn't Work"

**Solution**:
1. Check ADMIN_PASSWORD is set correctly
2. Try clearing browser cache
3. Use exact password you set

---

## Security Best Practices

✅ **Never commit these to GitHub**
- Firebase credentials stay in `.gitignore`
- Admin password never in code

✅ **Use Strong Passwords**
- Mix of uppercase, lowercase, numbers, symbols
- At least 12 characters

✅ **Keep FIREBASE_CONFIG Private**
- Only add in Render environment
- Never share publicly

✅ **Rotate Passwords Regularly**
- Change ADMIN_PASSWORD every 3-6 months

---

## Testing Your Variables

After adding variables:

1. Visit your Render app URL
2. Go to `/admin`
3. Enter admin password
4. Should login successfully ✅

If it doesn't work:
- Check Render logs
- Verify variables are saved
- Re-check values

---

## Quick Reference

**File**: `ENVIRONMENT_VARIABLES.md`  
**Deployment Guide**: `RENDER_DEPLOYMENT_GUIDE.md`  
**GitHub Repo**: https://github.com/Istemamahmed20445/sma-exam-system  

---

**Last Updated**: October 24, 2025

