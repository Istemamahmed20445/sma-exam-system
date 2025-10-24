// Admin Panel JavaScript
// This file contains utility functions for the admin panel

// Confirm before leaving page with unsaved changes
let unsavedChanges = false;

window.addEventListener('beforeunload', function(e) {
    if (unsavedChanges) {
        e.preventDefault();
        e.returnValue = 'You have unsaved changes. Are you sure you want to leave?';
        return e.returnValue;
    }
});

// Mark form as having unsaved changes
function markDirty() {
    unsavedChanges = true;
}

// Mark form as saved
function markClean() {
    unsavedChanges = false;
}

// Add question number labels dynamically
function addQuestionNumbers() {
    const questions = document.querySelectorAll('.question-editor');
    questions.forEach((question, index) => {
        const header = question.querySelector('.question-header h3');
        if (header && !header.textContent.includes('Question')) {
            header.textContent = `Question ${index + 1}`;
        }
    });
}

// Validate form before submission
function validateExamForm() {
    const title = document.getElementById('exam-title');
    const duration = document.getElementById('exam-duration');
    const passingMarks = document.getElementById('passing-marks');

    if (!title || !title.value.trim()) {
        alert('Please enter an exam title');
        title.focus();
        return false;
    }

    if (!duration || duration.value < 1) {
        alert('Duration must be at least 1 minute');
        duration.focus();
        return false;
    }

    if (!passingMarks || passingMarks.value < 0 || passingMarks.value > 100) {
        alert('Passing marks must be between 0 and 100');
        passingMarks.focus();
        return false;
    }

    return true;
}

// Export results to CSV
function exportToCSV(results) {
    if (!results || results.length === 0) {
        alert('No results to export');
        return;
    }

    const headers = ['Student Name', 'Exam', 'Score', 'Total Questions', 'Percentage', 'Date'];
    const rows = results.map(result => [
        result.student_name,
        result.exam_title,
        result.score,
        result.total_questions,
        result.percentage,
        new Date(result.submitted_at).toLocaleString()
    ]);

    const csvContent = [
        headers.join(','),
        ...rows.map(row => row.map(cell => `"${cell}"`).join(','))
    ].join('\n');

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    
    link.setAttribute('href', url);
    link.setAttribute('download', `exam_results_${new Date().toISOString().split('T')[0]}.csv`);
    link.style.visibility = 'hidden';
    
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Show loading spinner
function showLoading(element) {
    element.innerHTML = '<div class="loading">Loading...</div>';
}

// Show error message
function showError(element, message) {
    element.innerHTML = `<div class="error">${message}</div>`;
}

// Format date/time for display
function formatDateTime(timestamp) {
    if (!timestamp) return 'N/A';
    
    const date = timestamp.toDate ? timestamp.toDate() : new Date(timestamp);
    return date.toLocaleString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Handle image upload with preview
function handleImageUpload(input, previewContainer, callback) {
    if (!input.files || input.files.length === 0) return;

    const file = input.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        const img = document.createElement('img');
        img.src = e.target.result;
        img.style.maxWidth = '100%';
        img.style.maxHeight = '200px';
        
        previewContainer.innerHTML = '';
        previewContainer.appendChild(img);
        
        if (callback) {
            callback(file);
        }
    };

    reader.readAsDataURL(file);
}

// Debounce function for search/filter inputs
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Initialize admin features when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    // Add form change listeners
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('change', markDirty);
        form.addEventListener('submit', markClean);
    });

    // Initialize tooltips or other interactive elements
    console.log('Admin panel initialized');
});

