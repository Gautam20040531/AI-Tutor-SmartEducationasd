from fastapi import FastAPI, HTTPException
import joblib
import random
import json
import numpy as np
from pydantic import BaseModel

# Load trained chatbot model
try:
    model = joblib.load("chatbot/model.pkl")
    with open("chatbot/intents.json", "r") as file:
        intents = json.load(file)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

app = FastAPI(title="AI Chatbot")

class Message(BaseModel):
    message: str

# Preprocessing function
def preprocess_input(text):
    return [ord(c) for c in text.lower()[:20]]  # Convert text to numerical features

@app.post("/chat/")
def chat(message: Message):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded.")

    user_input = message.message
    input_data = np.array([preprocess_input(user_input)])

    # Predict intent
    intent_idx = model.predict(input_data)[0]
    intent_tag = list(intents["intents"].keys())[intent_idx]

    # Choose a random response from matched intent
    response = random.choice(intents["intents"][intent_tag]["responses"])
    return {"response": response}
