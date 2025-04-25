"""
This module defines the API routes for managing ToDo items in the application.
It includes endpoints for CRUD operations on ToDo items.
"""

from fastapi import APIRouter, HTTPException
from typing import List, Optional
from app.models.todo_model import ToDoItem
from app.db.fake_db import todo_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=List[ToDoItem])
def get_all_todos(completed: Optional[bool] = None) -> List[ToDoItem]:
    """
    Retrieves all ToDo items, optionally filtered by completion status.

    Args:
        completed (Optional[bool]): Filter for completed or incomplete ToDo items.

    Returns:
        List[ToDoItem]: A list of ToDo items matching the filter criteria.
    """
    if completed is None:
        return todo_db
    return [todo for todo in todo_db if todo.completed == completed]


@router.get("/{todo_id}", response_model=ToDoItem)
def get_todo(todo_id: int) -> ToDoItem:
    """
    Retrieves a specific ToDo item by its ID.

    Args:
        todo_id (int): The unique identifier of the ToDo item.

    Returns:
        ToDoItem: The ToDo item with the specified ID.

    Raises:
        HTTPException: If the ToDo item is not found.
    """
    for todo in todo_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="ToDo not found")


@router.post("/", response_model=ToDoItem)
def create_todo(todo: ToDoItem) -> ToDoItem:
    """
    Creates a new ToDo item and adds it to the database.

    Args:
        todo (ToDoItem): The ToDo item to be created.

    Returns:
        ToDoItem: The newly created ToDo item.

    Raises:
        HTTPException: If a ToDo item with the same ID already exists.
    """
    if any(t.id == todo.id for t in todo_db):
        raise HTTPException(status_code=400, detail="ToDo with this ID already exists")
    todo_db.append(todo)
    return todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: int) -> dict:
    """
    Deletes a specific ToDo item by its ID.

    Args:
        todo_id (int): The unique identifier of the ToDo item to delete.

    Returns:
        dict: A message confirming the deletion of the ToDo item.

    Raises:
        HTTPException: If the ToDo item is not found.
    """
    for i, todo in enumerate(todo_db):
        if todo.id == todo_id:
            del todo_db[i]
            return {"message": f"ToDo {todo_id} deleted"}
    raise HTTPException(status_code=404, detail="ToDo not found")
