const display = document.getElementById("display")

function appendToDisplay(input) {
    display.value += input;
}

function clearDisplay() {
    display.value = "";
}

function calculate() {
    try {
        display.value = eval(display.value);
    }
    catch (error) {
            display.value = "Error!";
        }
}
document.addEventListener('DOMContentLoaded', (event) => {
    const messageElement = document.getElementById('linkedin');

    messageElement.addEventListener('mouseover', () => {
        messageElement.querySelector('p').textContent = 'https://www.linkedin.com/in/yusuf-t-296635232/';
    });

    messageElement.addEventListener('mouseout', () => {
        messageElement.querySelector('p').textContent = 'Linkedin';
    });
});

document.addEventListener('DOMContentLoaded', (event) => {
    const messageElement = document.getElementById('gitHub');

    messageElement.addEventListener('mouseover', () => {
        messageElement.querySelector('p').textContent = 'https://github.com/josepyt';
    });

    messageElement.addEventListener('mouseout', () => {
        messageElement.querySelector('p').textContent = 'GitHub';
    });
});

