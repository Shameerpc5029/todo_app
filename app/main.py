"""
This module initializes the FastAPI application and sets up the API routes.
It also defines the root endpoint for the ToDo API.
"""

from fastapi import FastAPI
from app.routes.todo_routes import router

app = FastAPI()

app.include_router(router)


@app.get("/")
def read_root() -> dict[str, str]:
    """
    Handles the root endpoint of the API.

    Returns:
        dict[str, str]: A welcome message for the ToDo API.
    """
    return {"message": "Welcome to the ToDo API!"}
