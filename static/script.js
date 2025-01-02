'use strict';

document.querySelector('.start--btn').addEventListener('click', async (e) => {
    e.preventDefault();
    const delay = document.querySelector('.delay').value;
    const botSpeed = document.querySelector('.bot--speed').value;
    const response = await fetch('/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            delay: parseFloat(delay),
            botSpeed: parseFloat(botSpeed)
        })
    });
    const result = await response.json();
    document.querySelector('.response').textContent = result.status || result.error;
});

document.querySelector('.stop--btn').addEventListener('click', async (e) => {
    e.preventDefault();
    const response = await fetch('/stop', { method: 'POST' });
    const result = await response.json();
    document.querySelector('.response').textContent = result.status || result.error;
});
