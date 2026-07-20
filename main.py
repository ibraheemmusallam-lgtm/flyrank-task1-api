from fastapi import FastAPI

"""
FastAPI is the framework class.
app is our server application.
@app.get("/") connects GET / to the function below it.
Returning a Python dictionary makes FastAPI send JSON.
"""
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, server"}