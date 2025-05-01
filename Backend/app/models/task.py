
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    title: str
    id: Optional[int] = None
    description: Optional[str] = None
    completed: bool = False

    