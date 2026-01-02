from fastapi import FastAPI
from config import *

app = FastAPI(
    title="Semantic Search Service",
    description="Backend service for hybrid semantic + keyword search",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"name": "Semantic Search Service", "status": "ok", "docs": "/docs"}

