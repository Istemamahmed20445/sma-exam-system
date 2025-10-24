# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Test Firebase Connection
```bash
python test_firebase.py
```

You should see: ✅ Firebase connection test PASSED!

### Step 3: Run the Application
```bash
python app.py
```

### Step 4: Access the Application
- **Student Interface**: http://localhost:5000
- **Admin Panel**: http://localhost:5000/admin

### Step 5: Login to Admin Panel
- Password: `admin123` (change this in `.env` file)

---

## 📝 Creating Your First Exam

1. Go to Admin Panel → Create New Exam
2. Enter exam details:
   - Title: "Basic Medical Sciences - Test 1"
   - Duration: 60 minutes
   - Passing Marks: 60%
3. Click "Add Question"
4. Fill in the question:
   - Question text
   - Upload question image (optional)
   - Add 4-5 options
   - Select correct answer (radio button)
   - Add explanation
   - Upload explanation image (optional)
5. Click "Save Exam"

### Quick Tips
- Use clear, concise question text
- Keep images under 500KB for faster loading
- Add meaningful explanations to help students learn
- Test your exam before publishing

---

## 🎓 Student Exam Flow

1. Student visits http://localhost:5000
2. Selects an exam from the list
3. Enters their name
4. Starts the exam
5. Navigates through questions
6. Timer counts down automatically
7. Submits when finished (or auto-submits)
8. Views detailed results with explanations

---

## 🔧 Common Issues

### "Failed to load exams"
- Check that Firebase is properly configured
- Run `python test_firebase.py` to verify connection

### "Image upload failed"
- Check Firebase Storage is enabled
- Verify storage bucket: `mock-exam-sma.firebasestorage.app`
- Keep images under 2MB

### "Admin login not working"
- Check `.env` file exists
- Verify `ADMIN_PASSWORD` is set correctly
- Restart Flask app after changing `.env`

---

## 🌐 Deploying to Render

See the full deployment guide in `README.md`

---

## 📊 Usage Stats

- Currently handling: 0 exams, 0 results
- Capacity: 400-500 students/month
- Cost: ~$5-15/month

---

## Need Help?

Check the full documentation in `README.md` or contact your system administrator.

