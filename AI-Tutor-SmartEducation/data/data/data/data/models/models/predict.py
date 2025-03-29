import tensorflow as tf
import joblib
import numpy as np

# Load AI Model (Deep Learning)
ai_model = tf.keras.models.load_model("models/ai_model.h5")

# Load KNN Model (ML)
knn_model = joblib.load("models/knn_model.pkl")

# Function to make predictions
def predict(study_hours, attendance, previous_score):
    input_data = np.array([[study_hours, attendance, previous_score]])
    input_data = input_data / np.max(input_data, axis=0)  # Normalize

    ai_prediction = ai_model.predict(input_data)[0][0]
    knn_prediction = knn_model.predict(input_data)[0]

    return {
        "AI Model Prediction": round(ai_prediction, 2),
        "KNN Model Prediction": round(knn_prediction, 2)
    }

# Example Prediction
result = predict(5, 90, 80)
print(result)
