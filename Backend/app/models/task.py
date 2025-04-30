
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    name: str
    id: Optional[int] = None
    description: Optional[str] = None
    completed: bool = False

    