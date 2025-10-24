// Student Exam JavaScript
// This file contains additional utility functions for the exam interface

// Prevent accidental page refresh/close during exam
window.addEventListener('beforeunload', function(e) {
    // Check if there's an active exam (not on results page)
    if (window.location.pathname.includes('/exam/')) {
        e.preventDefault();
        e.returnValue = 'Are you sure you want to leave? Your progress may be lost.';
        return e.returnValue;
    }
});

// Keyboard shortcuts for exam navigation
document.addEventListener('keydown', function(e) {
    // Ignore if user is typing in an input field
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
        return;
    }

    // Arrow keys for navigation
    if (e.key === 'ArrowLeft') {
        const prevBtn = document.getElementById('prev-btn');
        if (prevBtn && !prevBtn.disabled) {
            prevBtn.click();
        }
    } else if (e.key === 'ArrowRight') {
        const nextBtn = document.getElementById('next-btn');
        if (nextBtn && nextBtn.style.display !== 'none') {
            nextBtn.click();
        }
    }
});

// Add visual feedback for answered questions
function updateAnswerStatus() {
    // This function is called from exam.html inline script
    // to provide visual feedback when answering questions
}

// Accessibility: Add screen reader support
function announceQuestionChange(questionNum, totalQuestions) {
    const announcement = document.createElement('div');
    announcement.setAttribute('role', 'status');
    announcement.setAttribute('aria-live', 'polite');
    announcement.className = 'sr-only';
    announcement.textContent = `Question ${questionNum} of ${totalQuestions}`;
    document.body.appendChild(announcement);
    
    setTimeout(() => {
        document.body.removeChild(announcement);
    }, 1000);
}

// Add print-friendly styles for results
function addPrintStyles() {
    const style = document.createElement('style');
    style.textContent = `
        @media print {
            .exam-header, .sidebar, footer, .btn-primary {
                display: none !important;
            }
            .question-section {
                margin: 0 !important;
                padding: 20px !important;
            }
        }
    `;
    document.head.appendChild(style);
}

// Initialize print styles when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addPrintStyles);
} else {
    addPrintStyles();
}

