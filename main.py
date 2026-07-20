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

@app.post("/tasks", status_code=201) # endpoint
def create_task(task_data: dict): # receive request body which FastAPI parses the JSON to a Python dictionary and passes into task_data
    title = task_data.get("title") # extract "title" key from task_data

    if not isinstance(title, str) or not title.strip(): # if title isn't a string or empty string, return 400 error, we use not to reverse them from false to true 
        return JSONResponse( # validation error
            status_code=400,
            content={"error": "Title must be a non-empty string"},
        )

    next_id = max((task["id"] for task in tasks), default=0) + 1 # find the highest id and add 1 to it, default is 0 if there are no tasks

    new_task = {
        "id": next_id,
        "title": title.strip(),
        "done": False,
    }

    tasks.append(new_task)
    return new_task
"""
curl: sends an HTTP request.
-i: displays response headers and body.
-X POST: selects the POST method.
URL: selects /tasks.
\: continues the Git Bash command on the next line.
-H: says the request body contains JSON.
-d: provides the request body.
"""