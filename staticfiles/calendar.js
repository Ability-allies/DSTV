// calendar.js

// Function to generate the calendar for the current month
function generateCalendar() {
    const calendarElement = document.getElementById('calendar');

    // Get the current date
    const date = new Date();
    const year = date.getFullYear();
    const month = date.getMonth();

    // Get the first day of the month and the number of days in the month
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);
    const totalDays = lastDay.getDate();

    // Clear any existing days
    calendarElement.innerHTML = '';

    // Generate empty cells for days of the week
    const firstDayIndex = firstDay.getDay();
    for (let i = 0; i < firstDayIndex; i++) {
        const emptyCell = document.createElement('div');
        emptyCell.classList.add('day');
        calendarElement.appendChild(emptyCell);
    }

    // Generate day cells
    for (let day = 1; day <= totalDays; day++) {
        const dayCell = document.createElement('div');
        dayCell.classList.add('day');
        dayCell.textContent = day;

        // Add click event to each day cell
        dayCell.onclick = () => {
            // Redirect to the activity page for that day
            location.href = `activity.html?day=${day}&month=${month + 1}&year=${year}`;
        };

        calendarElement.appendChild(dayCell);
    }
}

// Call the function to generate the calendar on page load
window.onload = generateCalendar;
