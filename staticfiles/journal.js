document.getElementById('journal-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const journalEntry = document.getElementById('journal-entry').value;
    const feedbackArea = document.getElementById('feedback');

    // Simulate feedback based on the journal entry
    if (journalEntry) {
        feedbackArea.value = "Great job documenting today's events! Keep it up!";
        document.getElementById('journal-entry').value = ""; // Clear the journal entry
    }
});
