// Firebase client configuration
const firebaseConfig = {
  apiKey: "AIzaSyAcg_zC2kPHVrZGwvFY8isAEgksIf14has",
  authDomain: "mock-exam-sma.firebaseapp.com",
  projectId: "mock-exam-sma",
  storageBucket: "mock-exam-sma.firebasestorage.app",
  messagingSenderId: "349617836999",
  appId: "1:349617836999:web:706cac0ddacafd88ac7fe2"
};

// Initialize Firebase (only if Firebase SDK is included)
if (typeof firebase !== 'undefined') {
  firebase.initializeApp(firebaseConfig);
}

