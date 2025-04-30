from flask import Blueprint
from task_view import TaskView

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

task_view = TaskView()

tasks_bp.route('/', methods=['GET'])(task_view.get_tasks)

tasks_bp.route('/', methods=['POST'])(task_view.create_task)

tasks_bp.route('/<int:task_id>', methods=['GET'])(task_view.get_task)
 
tasks_bp.route('/<int:task_id>', methods=['PUT'])(task_view.update_task)

tasks_bp.route('/<int:task_id>', methods=['DELETE'])(task_view.delete_task)