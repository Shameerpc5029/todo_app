"""
This module defines the ToDoItem model used to represent a task in the ToDo app.
It uses Pydantic for data validation and serialization of ToDo item attributes.
"""

from pydantic import BaseModel
from typing import Optional


class ToDoItem(BaseModel):
    """
    Represents a ToDo item with attributes for id, title, description, and status.
    """

    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
