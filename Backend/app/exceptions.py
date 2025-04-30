from werkzeug.exceptions import HTTPException


class CreateTaskException(HTTPException):
    code = 403
    description = "Failed to create task."
        

class TaskNotFoundException(HTTPException):
    code = 404
    description = "Task not found."
        

class TaskAlreadyExistsException(HTTPException):
    code = 409
    description = "Task already exists."


class TaskUpdateException(HTTPException):
    code = 403
    description = "Failed to update task."


class TaskDeleteException(HTTPException):
    code = 403
    description = "Failed to delete task."


class GetTasksException(HTTPException):
    code = 500
    description = "Failed to get tasks."