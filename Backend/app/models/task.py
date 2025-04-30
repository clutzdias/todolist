
from typing import Optional


class Task:
    id: Optional[int]
    name: str
    description: str
    completed: bool

    def __init__(self, id: int, name: str, description: str, completed: bool):
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f"Task(id={self.id}, name='{self.name}', description='{self.description}', completed='{self.completed}')"