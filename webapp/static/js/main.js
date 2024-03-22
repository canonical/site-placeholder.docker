// Scroll to the bottom of the logs
function scrollLogs() {
  let codeBox = document.getElementById("code-box");
  codeBox.scrollTo(0, codeBox.offsetTop);
}
window.addEventListener("load", scrollLogs);

// Disable restart button if build is currently in progress
function toggleRestartButton() {
  let button = document.getElementById("restart-button");

  if (button.getAttribute("data-building") === "True") {
    button.setAttribute("disabled", "");
  }
}
window.addEventListener("load", toggleRestartButton);

function submitRestartRequest() {
  let button = document.getElementById("restart-button");
  button.setAttribute("disabled", "");
  button.setAttribute("data-building", "True");
  button.innerHTML = "Restarting...";

  let xhr = new XMLHttpRequest();
  xhr.open("GET", "/restart-build", (result) => result.responseText);
  xhr.send();
}
