import json
import joblib
import numpy as np
from sklearn.neural_network import MLPClassifier

# Load training data
with open("chatbot/intents.json", "r") as file:
    intents = json.load(file)

# Prepare dataset
X_train = []
y_train = []
intent_labels = list(intents["intents"].keys())

for label_idx, (intent, data) in enumerate(intents["intents"].items()):
    for pattern in data["patterns"]:
        feature_vector = [ord(c) for c in pattern.lower()[:20]]
        X_train.append(feature_vector)
        y_train.append(label_idx)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Train a simple MLP classifier
model = MLPClassifier(hidden_layer_sizes=(16, 16), max_iter=500)
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "chatbot/model.pkl")

print("Chatbot model trained and saved!")
