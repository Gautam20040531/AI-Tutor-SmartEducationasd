import React, { useState } from "react";

function Chatbot() {
    const [message, setMessage] = useState("");
    const [response, setResponse] = useState("");

    const handleChat = async () => {
        const res = await fetch(`${process.env.REACT_APP_API_URL}/chat/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        });
        const data = await res.json();
        setResponse(data.response);
    };

    return (
        <div>
            <h2>AI Chatbot</h2>
            <input
                type="text"
                placeholder="Ask me anything..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
            />
            <button onClick={handleChat}>Send</button>
            {response && <p>Bot: {response}</p>}
        </div>
    );
}

export default Chatbot;
