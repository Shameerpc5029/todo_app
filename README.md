# ToDo App

A simple ToDo API built with FastAPI, designed for managing tasks with basic CRUD (Create, Read, Update, Delete) operations. This project uses an in-memory database for demonstration purposes and is ideal for learning or prototyping task management APIs.

## Features
- Create new ToDo items
- Retrieve all ToDo items or a specific item by ID
- Update and delete ToDo items
- Filter ToDo items by completion status

## Tech Stack
- **Python 3.13+**
- **FastAPI** for API endpoints
- **Pydantic** for data validation

## Project Structure
```
todo_app/
├── app/
│   ├── db/           # In-memory database (fake_db.py)
│   ├── models/       # Pydantic models (todo_model.py)
│   ├── routes/       # API routes (todo_routes.py)
│   └── main.py       # FastAPI app entrypoint
├── pyproject.toml    # Project dependencies
└── README.md         # Project documentation
```

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd todo_app
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   # or, if using pyproject.toml
   uv pip install .
   ```

## Running the Application
Start the FastAPI server:
```bash
fastapi run app.main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000)

## API Endpoints
- `GET /` — Welcome message
- `GET /todos/` — List all ToDo items (optionally filter by `completed`)
- `GET /todos/{todo_id}` — Get a specific ToDo item by ID
- `POST /todos/` — Create a new ToDo item
- `DELETE /todos/{todo_id}` — Delete a ToDo item by ID

## Example ToDo Item
```json
{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "completed": false
}
```

## License
This project is for educational purposes.

---
*Generated on 2025-04-24*