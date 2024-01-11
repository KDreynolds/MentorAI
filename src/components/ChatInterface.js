import React, { useState } from 'react';
import MessageList from './MessageList';

const ChatInterface = ({ messages, onSendMessage }) => {
  const [newMessage, setNewMessage] = useState('');

  const handleInputChange = (event) => {
    setNewMessage(event.target.value);
  };

  const handleSendClick = () => {
    if (newMessage.trim()) {
      onSendMessage(newMessage);
      setNewMessage('');
    }
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      handleSendClick();
    }
  };

  return (
    <div className="chat-interface">
      <MessageList messages={messages} />
      <div className="message-input-container">
        <input
          type="text"
          value={newMessage}
          onChange={handleInputChange}
          onKeyPress={handleKeyPress}
          placeholder="Type your message here..."
          className="message-input"
        />
        <button onClick={handleSendClick} className="send-message-button">
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatInterface;
