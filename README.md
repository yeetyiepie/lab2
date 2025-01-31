# Working with HTTP Actions and API Parameters

## Objectives
- Identify and differentiate different ways to parameterize an API
- Discuss HTTP methods and their uses based on best practices
- Use the HTTP methods and parameters to create a simple CRUD simulation API

## Instructions
1. Building on the sample code from the GitHub URL, revise the code to create a To-Do List API.
2. Here are the specifics:
   - On API run:
   ```python
   task_db = [
       {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
   ]
   ```
   
   - Endpoints:
     - `GET /tasks/{task_id}`
     - `POST /tasks`
     - `PATCH /tasks/{task_id}`
     - `DELETE /tasks/{task_id}`
     
   - Return values should be appropriate to the endpoints created.
   - Each endpoint should return `{ "status": "ok" }` for successful transactions, and `{ "error": <any error message related to the endpoint> }` for transaction issues.
   - Implement all necessary validations for entered data (null check, negative numbers, division by zero, etc.).

3. Turn in the GitHub repository link containing the following:
   - Python file with the API code.
   - `requirements.txt` listing the dependencies.
   - A screenshot of the Swagger UI (`http://127.0.0.1:8000/docs`).

## Features
- Create, retrieve, update, and delete tasks in a To-Do list.
- Uses FastAPI for efficient and easy API handling.
- Implements proper validation for input data.

## Requirements
- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/todo-api.git
   cd todo-api
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install fastapi uvicorn pydantic
   ```

## Running the API
Start the FastAPI server using Uvicorn:
```sh
uvicorn main:app --reload
```

## Usage
### Endpoints and Example Requests

#### Get a Task
```sh
GET http://127.0.0.1:8000/tasks/1
```

#### Create a New Task
```sh
POST http://127.0.0.1:8000/tasks
Content-Type: application/json

{
  "task_title": "New Task",
  "task_desc": "Task description",
  "is_finished": false
}
```

#### Update a Task
```sh
PATCH http://127.0.0.1:8000/tasks/1
Content-Type: application/json

{
  "is_finished": true
}
```

#### Delete a Task
```sh
DELETE http://127.0.0.1:8000/tasks/1
```

## API Documentation
Once the server is running, you can view the interactive API documentation at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License

