from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

router = APIRouter()

# Load AI Model
try:
    model = joblib.load("models/knn_model.pkl")  # Change based on model type
except Exception as e:
    print(f"Model Load Error: {e}")
    model = None

class InputData(BaseModel):
    features: list[float]

@router.post("/predict/")
def predict(data: InputData):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded.")
    
    try:
        prediction = model.predict([np.array(data.features)])
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
