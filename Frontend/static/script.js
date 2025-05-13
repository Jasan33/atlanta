function play() {
    let showContent = document.getElementById("words");
    showContent.style.display = 'block';
    startTimer(60); // Start timer with 60 seconds
}

const container = document.createElement("div");
container.classList.add("container");
document.body.appendChild(container);

function skip() {
    fetch("/random-word")
        .then(response => response.json())
        .then(data => {
            const word = data.word;

            document.getElementById("words").innerHTML = `<span class="word">${data.word}</span>`;
            inputHead.textContent = word;
            container.appendChild(inputHead);
        })
        .catch(error => {
            console.error("Error fetching word:", error);
        });
}

// Countdown Timer
function startTimer(duration) {
    let timerDisplay = document.getElementById("timer");
    let timeLeft = duration;
    let showPlayButton = document.getElementById("playbutton");

    showPlayButton.style.display = 'none';
    const interval = setInterval(() => {
        let minutes = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;
        timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

        if (--timeLeft < 0) {
            clearInterval(interval);
            timerDisplay.textContent = "Time's up!";
            showPlayButton.style.display = 'block';
            document.getElementById("words").style.display = 'none';
            // You can also trigger something here (e.g., show score or restart button)
        }
    }, 1000);
}

document.addEventListener("keydown", function (event) {
    if (event.key === "Tab") {
        event.preventDefault();
        location.reload();
    }
});