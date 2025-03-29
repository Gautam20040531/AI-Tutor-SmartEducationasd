import React from "react";
import AITutor from "./components/AITutor";
import Chatbot from "./components/Chatbot";

function App() {
    return (
        <div style={{ textAlign: "center", padding: "20px" }}>
            <h1>AI Tutor Smart Education</h1>
            <AITutor />
            <Chatbot />
        </div>
    );
}

export default App;
