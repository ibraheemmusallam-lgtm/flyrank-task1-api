from fastapi import FastAPI

"""
FastAPI is the framework class.
app is our server application.
@app.get("/") connects GET / to the function below it.
Returning a Python dictionary makes FastAPI send JSON.
GET / describes the API.
GET /health confirms the server is alive.
"""
app = FastAPI()

@app.get("/")
def read_root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"],
        "message": "Hello, server"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }