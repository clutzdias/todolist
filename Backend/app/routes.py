from flask import Blueprint, request, jsonify


tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    pass


@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    pass


@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    pass


@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    pass


@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    pass