from fastapi import FastAPI

app = FastAPI(
    title="DisasterReach AI API",
    description="Backend API for disaster risk mapping and healthcare access planning",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "DisasterReach AI API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }