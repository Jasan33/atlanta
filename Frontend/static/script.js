function play() {
    let ShowContent = document.getElementById("words");
    ShowContent.style.display = 'block';
}

const container = document.createElement("div");
container.classList.add("container");
document.body.appendChild(container);

function skip() {
    console.log("hei")
    const inputHead = document.createElement("p");
    inputHead.textContent = '{{ words }}';
    container.appendChild(inputHead);
}

document.addEventListener("keydown", function (event) {
    if (event.key === "Tab") {
        event.preventDefault(); // Prevents the default tab behavior (e.g., moving focus)
        location.reload(); // Reloads the page
    }
});