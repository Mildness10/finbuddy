document.addEventListener("DOMContentLoaded", function() {
    const textarea = document.getElementById('user-message');
    const messages = document.getElementById('messages');
    const form = document.getElementById('message-form');

    // Function to add a message to the chat interface
    function addMessage(message, sender) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.textContent = message;
        if (sender === 'bot') {
            messageElement.classList.add('bot-message');
            messageElement.style.backgroundColor = '#0d6efd';
            messageElement.style.padding = '10px';
            messageElement.style.borderRadius = '5px';

        } else {
            messageElement.classList.add('user-message');
            messageElement.style.backgroundColor = '#ffffff';
            messageElement.style.padding = '10px'
            messageElement.style.borderRadius = '5px';

        }
        messages.appendChild(messageElement);
        // Scroll to the bottom of the chat container
        messages.scrollTop = messages.scrollHeight;
    }

    // Event listener for form submission
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const userMessage = textarea.value.trim();
        if (userMessage === '') return;
        addMessage(userMessage, 'user');
        
        
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.startsWith(`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        
        const csrftoken = getCookie('csrftoken');
        // Send user message to backend for processing
        fetch('/finadvisor/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({ userMessage: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            const botResponse = data.response;
            addMessage(botResponse, 'bot');
        })
        .catch(error => {
            console.error('Error:', error);
        });
        
        textarea.value = ''; // Clear the textarea
    });
});