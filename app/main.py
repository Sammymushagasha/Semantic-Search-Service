from fastapi import FastAPI

# Creates the web app and its API documentation details.
app = FastAPI(
    title="Semantic Search Service",
    description="Backend service for hybrid semantic + keyword search",
    version="0.1.0",
)


# Lets you check whether the app is running.
@app.get("/health")
def health_check():
    return {"status": "ok"}


# Shows the app name and where to find the API docs.
@app.get("/")
def root():
    return {"name": "Semantic Search Service", "status": "ok", "docs": "/docs"}
