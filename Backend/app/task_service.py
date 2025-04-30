from .exceptions import (
    CreateTaskException,
    GetTasksException, 
    TaskAlreadyExistsException,
    TaskDeleteException,
    TaskNotFoundException,
    TaskUpdateException
)
from .database.task_repository import TaskRepository
from .models.task import Task

class TaskService:
    def __init__(self):
        self.repository = TaskRepository()


    def create_task(self, task: Task) -> Task:
        try:
            existing_task = self.repository.get_task_by_name(task.name)
            if existing_task:
                raise TaskAlreadyExistsException(f"Task with name {task.name} already exists.")
            return self.repository.create_task(task)
        except Exception as e:
            raise CreateTaskException(f"Failed to create task: {str(e)}") from e
    

    def get_task(self, task_id: int) -> Task:
        try:
            return self.repository.get_task(task_id)
        except Exception as e:
            raise TaskNotFoundException(f"Task with id {task_id} not found.") from e
    

    def update_task(self, task: Task) -> Task:
        try:
            existing_task = self.repository.get_task(task.id)
            if not existing_task:
                raise TaskNotFoundException(f"Task with id {task.id} not found.")
            return self._update_task(task)
        except Exception as e:
            raise TaskUpdateException(f"Failed to update task: {str(e)}") from e
        
    
    def delete_task(self, task_id: int) -> bool:
        try:
            return self.repository.delete_task(task_id)
        except Exception as e:
            raise TaskDeleteException(f"Failed to delete task with id {task_id}.") from e
       
    
    def get_tasks(self, only_completed: bool = False) -> list[Task]:
        try:
            return self.repository.get_tasks(only_completed)
        except Exception as e:
            raise GetTasksException(f"Failed to get tasks: {str(e)}") from e
    
