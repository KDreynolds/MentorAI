import React, { useState } from 'react';
import './App.css';
import ChatInterface from './components/ChatInterface';

function App() {
  const [messages, setMessages] = useState([]);

  const handleNewUserMessage = async (newMessage) => {
    // Update the state to include the new user message
    setMessages([...messages, { text: newMessage, isUser: true }]);

    try {
      // Send the message to the ChatGPT API and wait for the response
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: newMessage }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      // Update the state to include the new bot message
      setMessages([...messages, { text: newMessage, isUser: true }, { text: data.reply, isUser: false }]);
    } catch (error) {
      console.error('Failed to send message:', error);
      // Optionally, handle the error by displaying a message to the user
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>MentorAI</h1>
        <p>Your virtual senior developer mentor.</p>
      </header>
      <main>
        <ChatInterface messages={messages} onSendMessage={handleNewUserMessage} />
      </main>
    </div>
  );
}

export default App;
