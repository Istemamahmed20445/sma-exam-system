# Shahriar's Medical Academy Mock Exam System

A comprehensive MCQ-based mock exam system built with Flask and Firebase for Shahriar's Medical Academy.

## Features

- **Student Interface**: Clean, distraction-free exam interface with live timer
- **Admin Panel**: Create, edit, and manage exams with questions, images, and explanations
- **Image Support**: Upload images for questions and explanations
- **Timer**: Automatic exam submission when time expires
- **Results**: Detailed review showing correct answers and explanations
- **Firebase Integration**: Cloud-based database and storage

## Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python Flask
- **Database**: Firebase Firestore
- **Storage**: Firebase Storage
- **Deployment**: Render

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Firebase account and project
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Mock 3.0"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Firebase**
   - Download your Firebase service account JSON file
   - Place it in the project root as `firebase_config.json`
   - The file is already included in `.gitignore` for security

5. **Configure environment variables**
   - Copy `.env.example` to `.env`
   - Edit `.env` and set your admin password:
     ```
     ADMIN_PASSWORD=your_secure_password_here
     SECRET_KEY=your_secret_key_here
     ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access the application**
   - Student interface: http://localhost:5000
   - Admin panel: http://localhost:5000/admin

## Configuration

### Firebase Setup

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create a new project or use existing project
3. Enable Firestore Database
4. Enable Firebase Storage
5. Create a service account and download the JSON credentials
6. Place the JSON file in the project root as `firebase_config.json`

### Firebase Collections Structure

**exams** collection:
- `title` (string)
- `duration` (number, minutes)
- `passing_marks` (number, percentage)
- `questions` (array of objects)
- `created_at` (timestamp)
- `updated_at` (timestamp)

**results** collection:
- `student_name` (string)
- `exam_id` (string)
- `exam_title` (string)
- `score` (number)
- `total_questions` (number)
- `percentage` (number)
- `answers` (array of numbers)
- `submitted_at` (timestamp)

## Deployment to Render

1. **Create a Render account** at https://render.com

2. **Connect your repository**
   - Link your GitHub/GitLab repository
   - Render will auto-detect Flask

3. **Configure environment variables**
   - Go to your service settings
   - Add these environment variables:
     - `ADMIN_PASSWORD`: Your admin password
     - `SECRET_KEY`: Your Flask secret key
     - `PYTHON_VERSION`: 3.11.0

4. **Upload Firebase credentials**
   - In Render dashboard, go to your service
   - Navigate to "Environment" tab
   - Upload `firebase_config.json` or add the content as environment variable

5. **Build settings**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

6. **Deploy**
   - Click "Deploy" and wait for build to complete
   - Your app will be live at `https://your-app.onrender.com`

## Usage

### For Administrators

1. **Login**: Access `/admin` and enter your password
2. **Create Exam**: Click "Create New Exam"
3. **Add Questions**: Click "Add Question" for each question
4. **Upload Images**: Click on image upload buttons to add question/explanation images
5. **Set Correct Answer**: Select the radio button for the correct option
6. **Save Exam**: Click "Save Exam" when finished
7. **View Results**: See all student results in the dashboard
8. **Delete Results**: Remove individual results if needed

### For Students

1. **Select Exam**: Choose an exam from the home page
2. **Enter Name**: Provide your name to start
3. **Take Exam**: Answer questions using the interface
4. **Navigate**: Use Previous/Next buttons or question palette
5. **Submit**: Click "Submit Exam" when finished (or auto-submits when timer ends)
6. **View Results**: See your score and detailed review with explanations

## Features in Detail

### Timer
- Live countdown timer showing remaining time
- Visual warning when time is running out (last 60 seconds)
- Automatic submission when timer reaches zero

### Question Management
- Support for 4-5 options per question
- Question images (uploaded to Firebase Storage)
- Explanation images
- Text-based explanations

### Results Display
- Score and percentage
- Pass/Fail status
- Question-by-question review
- Correct answer highlighted
- Wrong answers shown
- Detailed explanations with images

## Scalability

The system is designed to handle:
- **400-500 students per month** easily
- **50-100 concurrent users** simultaneously
- **Cost**: ~$5-15/month at current scale

### Firebase Limits (Free Tier)
- Firestore: 50,000 reads/day, 20,000 writes/day
- Storage: 5 GB storage, 1 GB downloads/day

Upgrade to Blaze plan (pay-as-you-go) for higher limits.

## Security Considerations

- Admin authentication via password
- Firebase Admin SDK for secure database access
- Image upload validation
- Input sanitization
- Session management

## Troubleshooting

### Common Issues

1. **"Failed to load exams"**
   - Check Firebase configuration
   - Verify `firebase_config.json` is in project root
   - Check Firebase project permissions

2. **"Image upload failed"**
   - Check Firebase Storage rules
   - Verify storage bucket is configured
   - Check image file size (recommended: < 500KB)

3. **"Admin login not working"**
   - Check `.env` file exists
   - Verify `ADMIN_PASSWORD` is set correctly
   - Restart the Flask application

## Future Enhancements

- [ ] User authentication system
- [ ] Practice mode (no timer)
- [ ] Question categories and tags
- [ ] Difficulty levels
- [ ] Performance analytics dashboard
- [ ] Email notifications
- [ ] PDF certificate generation
- [ ] Export results to Excel/PDF
- [ ] Randomize question/option order

## License

© 2024 Shahriar's Medical Academy. All rights reserved.

## Support

For issues or questions, please contact the system administrator.

