from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_file
import firebase_admin
from firebase_admin import credentials, firestore, storage
import os
from datetime import datetime
import json
from dotenv import load_dotenv
import csv
import io

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-change-this-in-production')

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    # Try to load Firebase config from environment variable (for Render deployment)
    firebase_config_env = os.getenv('FIREBASE_CONFIG')
    if firebase_config_env:
        # Parse JSON from environment variable
        firebase_config = json.loads(firebase_config_env)
        cred = credentials.Certificate(firebase_config)
    else:
        # Fallback to file (for local development)
        cred = credentials.Certificate('firebase_config.json')
    
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'mock-exam-sma.firebasestorage.app'
    })

db = firestore.client()
bucket = storage.bucket()

# Admin password from environment
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')

# Helper function to check admin authentication
def is_admin():
    return session.get('admin_logged_in', False)

# ============================================
# STUDENT ROUTES
# ============================================

@app.route('/')
def index():
    """Landing page - list available exams"""
    return render_template('index.html')

@app.route('/exam/<exam_id>')
def exam(exam_id):
    """Exam interface"""
    return render_template('exam.html', exam_id=exam_id)

@app.route('/results/<result_id>')
def results(result_id):
    """Results page"""
    return render_template('results.html', result_id=result_id)

# ============================================
# ADMIN ROUTES
# ============================================

@app.route('/admin')
def admin_login():
    """Admin login page"""
    if is_admin():
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')

@app.route('/admin/login', methods=['POST'])
def admin_login_post():
    """Handle admin login"""
    password = request.json.get('password')
    if password == ADMIN_PASSWORD:
        session['admin_logged_in'] = True
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Invalid password'}), 401

@app.route('/admin/logout')
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/admin/dashboard')
def admin_dashboard():
    """Admin dashboard"""
    if not is_admin():
        return redirect(url_for('admin_login'))
    return render_template('admin_dashboard.html')

@app.route('/admin/exam/create')
@app.route('/admin/exam/edit/<exam_id>')
def admin_exam_editor(exam_id=None):
    """Create or edit exam"""
    if not is_admin():
        return redirect(url_for('admin_login'))
    return render_template('admin_exam_editor.html', exam_id=exam_id)

# ============================================
# API ROUTES
# ============================================

@app.route('/api/exams', methods=['GET'])
def get_exams():
    """Get all exams"""
    try:
        exams_ref = db.collection('exams')
        exams = exams_ref.stream()
        
        exams_list = []
        for exam in exams:
            exam_data = exam.to_dict()
            exam_data['exam_id'] = exam.id
            exams_list.append(exam_data)
        
        return jsonify({'success': True, 'exams': exams_list})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/exam/<exam_id>', methods=['GET'])
def get_exam(exam_id):
    """Get specific exam"""
    try:
        exam_ref = db.collection('exams').document(exam_id)
        exam = exam_ref.get()
        
        if not exam.exists:
            return jsonify({'success': False, 'error': 'Exam not found'}), 404
        
        exam_data = exam.to_dict()
        exam_data['exam_id'] = exam.id
        return jsonify({'success': True, 'exam': exam_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/exam/save', methods=['POST'])
def save_exam():
    """Save exam (create or update)"""
    if not is_admin():
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        data = request.json
        exam_id = data.get('exam_id')
        
        # Handle the case where exam_id is the string "None" from template
        if exam_id == 'None' or exam_id is None:
            exam_id = None
        
        exam_data = {
            'title': data.get('title'),
            'duration': int(data.get('duration')),
            'passing_marks': int(data.get('passing_marks')),
            'questions': data.get('questions', []),
            'updated_at': firestore.SERVER_TIMESTAMP
        }
        
        if exam_id:
            # Update existing exam
            db.collection('exams').document(exam_id).update(exam_data)
        else:
            # Create new exam
            exam_data['created_at'] = firestore.SERVER_TIMESTAMP
            doc_ref = db.collection('exams').add(exam_data)
            exam_id = doc_ref[1].id
        
        return jsonify({'success': True, 'exam_id': exam_id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/exam/delete/<exam_id>', methods=['DELETE'])
def delete_exam(exam_id):
    """Delete exam"""
    if not is_admin():
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        db.collection('exams').document(exam_id).delete()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/submit', methods=['POST'])
def submit_exam():
    """Submit exam answers"""
    try:
        data = request.json
        exam_id = data.get('exam_id')
        student_name = data.get('student_name')
        student_email = data.get('student_email', '')
        answers = data.get('answers', [])
        
        # Get exam data
        exam_ref = db.collection('exams').document(exam_id)
        exam = exam_ref.get()
        
        if not exam.exists:
            return jsonify({'success': False, 'error': 'Exam not found'}), 404
        
        exam_data = exam.to_dict()
        questions = exam_data.get('questions', [])
        
        # Calculate score
        score = 0
        for i, answer in enumerate(answers):
            if i < len(questions):
                correct_answer = questions[i].get('correct_answer')
                if answer == correct_answer:
                    score += 1
        
        total_questions = len(questions)
        percentage = (score / total_questions * 100) if total_questions > 0 else 0
        
        # Save result
        result_data = {
            'student_name': student_name,
            'student_email': student_email,
            'exam_id': exam_id,
            'exam_title': exam_data.get('title'),
            'score': score,
            'total_questions': total_questions,
            'percentage': round(percentage, 2),
            'answers': answers,
            'submitted_at': firestore.SERVER_TIMESTAMP
        }
        
        result_ref = db.collection('results').add(result_data)
        result_id = result_ref[1].id
        
        return jsonify({
            'success': True,
            'result_id': result_id,
            'score': score,
            'total_questions': total_questions,
            'percentage': round(percentage, 2)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/results', methods=['GET'])
def get_results():
    """Get all results"""
    if not is_admin():
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        results_ref = db.collection('results')
        results = results_ref.order_by('submitted_at', direction=firestore.Query.DESCENDING).stream()
        
        results_list = []
        for result in results:
            result_data = result.to_dict()
            result_data['result_id'] = result.id
            # Convert timestamp
            if 'submitted_at' in result_data:
                result_data['submitted_at'] = result_data['submitted_at'].isoformat()
            results_list.append(result_data)
        
        return jsonify({'success': True, 'results': results_list})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/result/<result_id>', methods=['GET'])
def get_result(result_id):
    """Get specific result"""
    try:
        result_ref = db.collection('results').document(result_id)
        result = result_ref.get()
        
        if not result.exists:
            return jsonify({'success': False, 'error': 'Result not found'}), 404
        
        result_data = result.to_dict()
        result_data['result_id'] = result.id
        
        # Get exam data
        exam_ref = db.collection('exams').document(result_data['exam_id'])
        exam = exam_ref.get()
        result_data['exam'] = exam.to_dict()
        
        return jsonify({'success': True, 'result': result_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/result/delete/<result_id>', methods=['DELETE'])
def delete_result(result_id):
    """Delete result"""
    if not is_admin():
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        db.collection('results').document(result_id).delete()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    """Upload image to Firebase Storage"""
    if not is_admin():
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400
        
        # Upload to Firebase Storage
        blob = bucket.blob(f'images/{datetime.now().timestamp()}_{file.filename}')
        blob.upload_from_file(file)
        blob.make_public()
        
        return jsonify({'success': True, 'url': blob.public_url})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/bulk-upload-template')
def download_template():
    """Download CSV template for bulk question upload"""
    if not is_admin():
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        # Create CSV template in memory
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Write header
        writer.writerow(['question_text', 'option_1', 'option_2', 'option_3', 'option_4', 'option_5', 'correct_answer', 'explanation'])
        
        # Write example rows
        writer.writerow([
            'What is the powerhouse of the cell?',
            'Nucleus',
            'Mitochondria',
            'Ribosome',
            'Golgi Apparatus',
            '',
            '2',
            'Mitochondria is known as the powerhouse of the cell because it produces ATP'
        ])
        writer.writerow([
            'Normal resting heart rate for adults?',
            '40-60 bpm',
            '60-100 bpm',
            '100-120 bpm',
            '120-140 bpm',
            '',
            '2',
            'Normal resting heart rate ranges from 60-100 beats per minute'
        ])
        
        output.seek(0)
        
        # Create Flask response
        response = app.response_class(
            output.getvalue(),
            mimetype='text/csv',
            headers={'Content-Disposition': 'attachment; filename=question_template.csv'}
        )
        
        return response
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/bulk-upload-validate', methods=['POST'])
def validate_bulk_upload():
    """Validate CSV file and return preview"""
    if not is_admin():
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400
        
        # Read CSV using built-in csv module
        stream = io.StringIO(file.read().decode('utf-8'))
        reader = csv.DictReader(stream)
        
        # Validate columns
        required_columns = ['question_text', 'option_1', 'option_2', 'correct_answer', 'explanation']
        if not reader.fieldnames:
            return jsonify({'success': False, 'error': 'Invalid CSV file'}), 400
        
        missing_columns = [col for col in required_columns if col not in reader.fieldnames]
        if missing_columns:
            return jsonify({
                'success': False,
                'error': f'Missing columns: {", ".join(missing_columns)}'
            }), 400
        
        # Validate data
        errors = []
        questions = []
        
        for row_num, row in enumerate(reader, start=2):  # Start at 2 (row 1 is header)
            # Check required fields
            if not row.get('question_text') or not row['question_text'].strip():
                errors.append(f'Row {row_num}: Question text is required')
                continue
            
            # Get options
            options = []
            for i in range(1, 6):
                col_name = f'option_{i}'
                value = row.get(col_name, '').strip()
                if value:
                    options.append(value)
            
            if len(options) < 2:
                errors.append(f'Row {row_num}: At least 2 options required')
                continue
            
            # Validate correct answer
            try:
                correct_answer = int(row['correct_answer'])
                if correct_answer < 1 or correct_answer > len(options):
                    errors.append(f'Row {row_num}: Correct answer must be between 1 and {len(options)}')
                    continue
            except (ValueError, TypeError):
                errors.append(f'Row {row_num}: Correct answer must be a number')
                continue
            
            # Check explanation
            if not row.get('explanation') or not row['explanation'].strip():
                errors.append(f'Row {row_num}: Explanation is required')
                continue
            
            # Store valid question
            questions.append({
                'question_text': row['question_text'].strip(),
                'options': options,
                'correct_answer': correct_answer - 1,  # Convert to 0-based index
                'explanation': row['explanation'].strip(),
                'question_image_url': '',
                'explanation_image_url': ''
            })
        
        return jsonify({
            'success': True,
            'questions': questions,
            'errors': errors,
            'total_rows': row_num - 1,  # Exclude header
            'valid_questions': len(questions)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/bulk-upload-import', methods=['POST'])
def import_bulk_questions():
    """Import validated questions to an exam"""
    if not is_admin():
        return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    try:
        data = request.json
        exam_id = data.get('exam_id')
        questions = data.get('questions', [])
        
        if not exam_id:
            return jsonify({'success': False, 'error': 'Exam ID required'}), 400
        
        if not questions:
            return jsonify({'success': False, 'error': 'No questions to import'}), 400
        
        # Get exam
        exam_ref = db.collection('exams').document(exam_id)
        exam = exam_ref.get()
        
        if not exam.exists:
            return jsonify({'success': False, 'error': 'Exam not found'}), 404
        
        exam_data = exam.to_dict()
        existing_questions = exam_data.get('questions', [])
        
        # Add new questions (maintain serial/order)
        updated_questions = existing_questions + questions
        
        # Update exam
        exam_ref.update({
            'questions': updated_questions,
            'updated_at': firestore.SERVER_TIMESTAMP
        })
        
        return jsonify({
            'success': True,
            'imported': len(questions),
            'total_questions': len(updated_questions)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

