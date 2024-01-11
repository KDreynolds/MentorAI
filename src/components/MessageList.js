import React from 'react';
import './MessageList.css'; // Assuming you have a corresponding CSS file for styling

const MessageList = ({ messages }) => {
  return (
    <div className="message-list">
      {messages.map((message, index) => (
        <div key={index} className={`message-item ${message.isUser ? 'user-message' : 'bot-message'}`}>
          <div className="message-content">{message.text}</div>
        </div>
      ))}
    </div>
  );
};

export default MessageList;
