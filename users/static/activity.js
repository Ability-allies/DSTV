const urlParams = new URLSearchParams(window.location.search);
const selectedDate = urlParams.get('date');

const activities = {
    "2024-10-01": {
        advice: "Encourage social interactions with peers.",
        therapy: "Art therapy focusing on color recognition."
    },
    "2024-10-02": {
        advice: "Use visual aids to enhance learning.",
        therapy: "Storytelling session to enhance communication skills."
    },
    "2024-10-03": {
        advice: "Engage in physical activities.",
        therapy: "Outdoor play to develop motor skills."
    },
    "2024-10-04": {
        advice: "Introduce musical instruments for sensory development.",
        therapy: "Music therapy focusing on rhythm and movement."
    },
    "2024-10-05": {
        advice: "Explore different textures for sensory learning.",
        therapy: "Sensory play with different textures."
    },
    // Add more activities as needed
};

document.getElementById('selected-date').innerText = selectedDate;

if (activities[selectedDate]) {
    document.getElementById('advice-content').innerText = activities[selectedDate].advice;
    document.getElementById('therapy-content').innerText = activities[selectedDate].therapy;
} else {
    document.getElementById('advice-content').innerText = "No advice available for this date.";
    document.getElementById('therapy-content').innerText = "No therapy sessions available for this date.";
}
