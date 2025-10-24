# 🔍 Thumbnail Troubleshooting Guide

## Debugging Steps

### 1. **Check Browser Console**

Open browser DevTools (F12) and check the console for:

**On Homepage:**
- Should see: `Exams data: [...]` with exam objects
- Should see: `Exam: [Title] Thumbnail: [URL or undefined]`

**When Saving Exam:**
- Should see: `Saving exam with thumbnail: [URL or empty]`

---

### 2. **Verify Thumbnail Upload**

When creating/editing an exam:

1. Select an image file
2. Click **"Upload Thumbnail"**
3. Check for success message: "Thumbnail uploaded successfully!"
4. Verify the preview appears below the upload button
5. Look at hidden input value: Inspect element `<input type="hidden" id="thumbnail-url">`
   - Should have a Firebase Storage URL

---

### 3. **Check Firebase Database**

The thumbnail should be stored in the exam document:

**Firebase Console → Firestore → exams Collection**

Look for `thumbnail_url` field in your exam documents.

**If thumbnail_url field doesn't exist:**
- The exam was created before the thumbnail feature
- Need to edit and re-upload the thumbnail

**If thumbnail_url is empty string "" or null:**
- Check the upload process worked
- Verify "Upload Thumbnail" button was clicked before saving

---

### 4. **Common Issues**

### ❌ **Thumbnail Not Showing**

**Possible Causes:**

1. **Thumbnail not uploaded**
   - Solution: Make sure to click "Upload Thumbnail" button before saving exam

2. **Old exams without thumbnails**
   - Solution: Edit existing exams and add thumbnails

3. **Empty thumbnail_url value**
   - Solution: Upload thumbnail properly before saving

4. **Image URL is invalid**
   - Solution: Check Firebase Storage permissions

### ✅ **To Fix:**

1. Go to **Admin Dashboard**
2. Click **Edit** on the exam
3. Scroll to **"Thumbnail Image (Optional)"**
4. Click **"Choose File"** and select an image
5. **IMPORTANT:** Click **"Upload Thumbnail"** button
6. Wait for success message
7. Verify preview appears
8. Then click **"Save Exam"**

---

### 5. **Verify Upload Process**

The complete flow should be:

```
1. Select image file
   ↓
2. Preview appears (local preview)
   ↓
3. Click "Upload Thumbnail"
   ↓
4. Image uploads to Firebase Storage
   ↓
5. Hidden input gets URL value
   ↓
6. Success message appears
   ↓
7. Click "Save Exam"
   ↓
8. thumbnail_url saved to Firestore
   ↓
9. Homepage displays thumbnail
```

---

### 6. **Test with Browser Console**

**When on Homepage:**
```javascript
// Check what exams data looks like
fetch('/api/exams')
  .then(r => r.json())
  .then(d => console.log(d.exams))
```

Look for `thumbnail_url` field in each exam object.

---

### 7. **Manual Test**

Create a brand new exam:

1. Admin Dashboard → Create New Exam
2. Fill in all required fields
3. **Add thumbnail image**:
   - Choose file
   - Click "Upload Thumbnail"
   - See success message
4. Add at least one question
5. Save exam
6. Go to homepage
7. Check if thumbnail appears

---

## 🎯 Quick Fix Checklist

- [ ] Selected an image file
- [ ] Clicked "Upload Thumbnail" button
- [ ] Saw success message
- [ ] Preview appeared
- [ ] Saved the exam
- [ ] Checked Firebase Firestore for thumbnail_url field
- [ ] Verified thumbnail_url has a valid URL
- [ ] Cleared browser cache and refreshed homepage

---

## 💡 Need More Help?

Check browser console for errors and share:
1. What console shows for exam data
2. Whether thumbnail_url field exists in Firebase
3. Any error messages

