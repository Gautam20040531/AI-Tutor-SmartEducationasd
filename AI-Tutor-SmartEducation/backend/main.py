from fastapi import FastAPI
from backend.api import router as api_router

app = FastAPI(title="AI Tutor Smart Education API")

app.include_router(api_router)

@app.get("/")
def home():
    return {"message": "Welcome to AI Tutor API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
