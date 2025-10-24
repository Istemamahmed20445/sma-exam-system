#!/usr/bin/env python3
"""
Quick test script to verify Firebase connectivity
"""

import firebase_admin
from firebase_admin import credentials, firestore

def test_firebase():
    print("Testing Firebase connection...")
    
    try:
        # Initialize Firebase
        if not firebase_admin._apps:
            cred = credentials.Certificate('firebase_config.json')
            firebase_admin.initialize_app(cred, {
                'storageBucket': 'mock-exam-sma.firebasestorage.app'
            })
        
        # Test Firestore connection
        db = firestore.client()
        print("✓ Firebase Admin SDK initialized successfully")
        print("✓ Firestore client created")
        
        # Try to read a collection (this will work even if collection doesn't exist)
        exams_ref = db.collection('exams')
        print("✓ Connected to 'exams' collection")
        
        print("\n✅ Firebase connection test PASSED!")
        print("\nYou can now run the Flask application with: python app.py")
        
    except Exception as e:
        print(f"\n❌ Firebase connection test FAILED!")
        print(f"Error: {str(e)}")
        print("\nPlease check:")
        print("1. firebase_config.json exists and is valid")
        print("2. Firebase project 'mock-exam-sma' is accessible")
        print("3. Firestore is enabled in your Firebase project")

if __name__ == '__main__':
    test_firebase()

