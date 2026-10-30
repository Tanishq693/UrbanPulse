from fastapi import FastAPI

app = FastAPI(title="UrbanPulse API")

@app.get("/")
def home():
    return {"message": "UrbanPulse API running"}

@app.get("/health")
def health():
    return {"status": "healthy"}