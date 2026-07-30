# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework in Python, including defining routes, handling request parameters, and working with Pydantic models for data validation.

## 📝 Tasks

### 🛠️ Set Up Your First API Endpoint

#### Description
Create a FastAPI application with a basic "Hello, World" endpoint and a health check endpoint that returns the API status.

#### Requirements
Completed program should:

- Install FastAPI and an ASGI server (e.g., `uvicorn`)
- Create a FastAPI app instance
- Define a `GET /` endpoint that returns a welcome message
- Define a `GET /health` endpoint that returns `{"status": "ok"}`

### 🛠️ Build a Task List CRUD API

#### Description
Create a set of RESTful endpoints to manage a simple in-memory task list. Use Pydantic models to validate request data.

#### Requirements
Completed program should:

- Define a Pydantic model `Task` with fields: `id` (int), `title` (str), `description` (str, optional), and `completed` (bool, default `False`)
- Implement `GET /tasks` to return the full list of tasks
- Implement `GET /tasks/{task_id}` to return a single task by ID (return 404 if not found)
- Implement `POST /tasks` to create a new task with auto-generated ID
- Implement `PUT /tasks/{task_id}` to update an existing task
- Implement `DELETE /tasks/{task_id}` to remove a task

### 🛠️ Add Query Parameters and Filtering

#### Description
Enhance the task list API with search and filtering capabilities using query parameters.

#### Requirements
Completed program should:

- Support a `?completed=true|false` query parameter on `GET /tasks` to filter by completion status
- Support a `?search=<keyword>` query parameter on `GET /tasks` to search tasks by title (case-insensitive partial match)
- When no query parameters are provided, return all tasks as before

## 📦 Starter Code

The `starter-code.py` file contains a skeleton FastAPI application with the initial setup. Complete the implementation by filling in the missing route handlers.
