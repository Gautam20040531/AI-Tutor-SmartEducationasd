import React, { useState } from "react";

function AITutor() {
    const [input, setInput] = useState("");
    const [prediction, setPrediction] = useState(null);

    const handlePredict = async () => {
        const response = await fetch(`${process.env.REACT_APP_API_URL}/predict/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ features: input.split(",").map(Number) }),
        });
        const data = await response.json();
        setPrediction(data.prediction);
    };

    return (
        <div>
            <h2>AI Tutor</h2>
            <input
                type="text"
                placeholder="Enter comma-separated numbers"
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />
            <button onClick={handlePredict}>Predict</button>
            {prediction && <p>Prediction: {prediction}</p>}
        </div>
    );
}

export default AITutor;
