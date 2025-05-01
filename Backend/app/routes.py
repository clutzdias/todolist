from flask import Blueprint
from .task_view import TaskView

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

task_view = TaskView()

tasks_bp.add_url_rule('/', view_func=task_view.get_tasks, methods=['GET'])

tasks_bp.add_url_rule('/', view_func=task_view.create_task, methods=['POST'])

tasks_bp.add_url_rule('/<int:task_id>', view_func=task_view.get_task, methods=['GET'])

tasks_bp.add_url_rule('/<int:task_id>', view_func=task_view.update_task, methods=['PUT'])

tasks_bp.add_url_rule('/<int:task_id>', view_func=task_view.delete_task, methods=['DELETE'])