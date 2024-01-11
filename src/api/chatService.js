// src/api/chatService.js

const sendChatMessage = async (message) => {
  try {
    // Send the message to the ChatGPT API and wait for the response
    const response = await fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.reply;
  } catch (error) {
    console.error('Failed to send message:', error);
    // Optionally, handle the error by displaying a message to the user
    // For now, we'll just return a placeholder error message
    return "Sorry, I'm having trouble understanding that right now. Please try again later.";
  }
};

export default sendChatMessage;
