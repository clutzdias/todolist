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
            existing_task = self.repository.get_task_by_title(task.title)
            if existing_task:
                raise TaskAlreadyExistsException(description=f"Task with title {task.title} already exists.")
            return self.repository.create_task(task)
        except Exception as e:
            raise CreateTaskException(description=f"Failed to create task: {str(e)}") from e
    

    def get_task(self, task_id: int) -> Task:
        try:
            return self.repository.get_task(task_id)
        except Exception as e:
            raise TaskNotFoundException(description=f"Task with id {task_id} not found.") from e
    

    def update_task(self, task: Task) -> Task:
        try:
            existing_task = self.repository.get_task(task.id)
            if not existing_task:
                raise TaskNotFoundException(description=f"Task with id {task.id} not found.")
            self.repository.update_task(task)
            return task
        except Exception as e:
            raise TaskUpdateException(description=f"Failed to update task: {str(e)}") from e
        
    
    def delete_task(self, task_id: int) -> bool:
        try:
            self.repository.delete_task(task_id)
        except Exception as e:
            raise TaskDeleteException(description=f"Failed to delete task with id {task_id}.") from e
       
    
    def get_tasks(self, only_completed: bool = False) -> list[Task]:
        try:
            return self.repository.get_tasks(only_completed)
        except Exception as e:
            raise GetTasksException(description=f"Failed to get tasks: {str(e)}") from e
    
