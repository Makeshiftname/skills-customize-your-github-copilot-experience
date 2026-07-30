from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task Manager API")


# ---------- Pydantic Models ----------

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


# ---------- In-Memory Database ----------

tasks_db: list[Task] = []
next_id: int = 1


# ---------- Route Handlers ----------

@app.get("/")
def root():
    # TODO: Return a welcome message
    pass


@app.get("/health")
def health_check():
    # TODO: Return {"status": "ok"}
    pass


@app.get("/tasks")
def list_tasks(completed: Optional[bool] = None, search: Optional[str] = None):
    """
    Return all tasks. Optionally filter by:
    - completed: true/false
    - search: case-insensitive keyword in title
    """
    # TODO: Implement filtering logic
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Return the task with the given ID, or raise 404
    pass


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global next_id
    # TODO: Create a new task with auto-generated ID
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    # TODO: Update fields of the task with the given ID
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Remove the task with the given ID
    pass
