import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017/")
MODEL_PATH = os.getenv("MODEL_PATH", "models/knn_model.pkl")
