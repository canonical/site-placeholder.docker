// Refresh the screen every 10 seconds
function refresh() {
    location.reload();
}
setTimeout(refresh, 10000);

// Scroll to the bottom of the logs
function scrollLogs() {
    let codeBox = document.getElementById('code-box');
    codeBox.scrollTo(0, codeBox.offsetTop);
}
window.addEventListener('load', scrollLogs);

// Disable restart button if build is currently in progress
function toggleRestartButton() {
    let button = document.getElementById('restart-button');

    if (button.getAttribute("data-building") === "True") {
        button.setAttribute("disabled", "");
    }   
}
window.addEventListener('load', toggleRestartButton);