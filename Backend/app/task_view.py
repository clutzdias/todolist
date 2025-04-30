from flask import jsonify, request
from werkzeug.exceptions import HTTPException

from .models.task import Task
from task_service import TaskService


class TaskView:
    def __init__(self):
        self.task_service = TaskService()


    def get_tasks(self):
        try:
            tasks = self.task_service.get_tasks()
            return jsonify([task.asdict() for task in tasks]), 200
        except HTTPException as e:
            raise e


    def get_task(self, task_id):
        try:
            task = self.task_service.get_task(task_id)
            return jsonify(task.asdict()), 200
        except HTTPException as e:
            raise e


    def update_task(self, task_id):
        try:
            data = request.get_json()
            task = self.task_service.update_task(task_id, data)
            return jsonify(task.asdict()), 200
        except HTTPException as e:
            raise e


    def create_task(self):
        try:
            data = request.get_json()
            task_obj = Task(**data)
            task = self.task_service.create_task(task_obj)
            return jsonify(task.asdict()), 201
        except HTTPException as e:
            raise e


    def delete_task(self, task_id):
        try:
            self.task_service.delete_task(task_id)
            return None, 204
        except HTTPException as e:
            raise e




