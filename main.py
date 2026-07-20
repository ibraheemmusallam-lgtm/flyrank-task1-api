from fastapi import FastAPI
from fastapi.responses import JSONResponse
"""
FastAPI is the framework class.
app is our server application.
@app.get("/") connects GET / to the function below it.
Returning a Python dictionary makes FastAPI send JSON.
GET / describes the API.
GET /health confirms the server is alive.
"""
app = FastAPI()
tasks = [
    {"id": 1, "title": "Learn FastAPI", "done": False},
    {"id": 2, "title": "Build a CRUD API", "done": False},
    {"id": 3, "title": "Test the API", "done": True},
]

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

"""
tasks is in-memory storage: restarting Python restores the original three tasks.
{task_id} is a changing path parameter.
task_id: int tells FastAPI it must be an integer.
The loop searches for a matching ID.
An unknown ID deliberately returns 404, not an empty 200.
"""

@app.get("/tasks")
def list_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return JSONResponse(
        status_code=404,
        content={"error": f"Task {task_id} not found"},
    )