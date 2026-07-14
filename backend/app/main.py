from fastapi import FastAPI
from app.routers import landlords

app = FastAPI(
    title="PropFlow AI",
    version="0.1.0",
    description="AI-powered Real Estate CRM"
)

app.include_router(landlords.router)

@app.get("/")
def root():
    return {"message": "Welcome to PropFlow AI 🚀"}

@app.get("/health")
def health():
    return {"status": "healthy"}