"""
This module provides a simulated in-memory database for managing ToDo items.
It uses a list to store and manipulate ToDoItem objects for testing purposes.
"""

from typing import List
from app.models.todo_model import ToDoItem

# Simulated in-memory DB
todo_db: List[ToDoItem] = []
