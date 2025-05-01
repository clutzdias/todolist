from flask import jsonify, request
from werkzeug.exceptions import HTTPException
from dataclasses import asdict

from .models.task import Task
from .task_service import TaskService


class TaskView:
    def __init__(self):
        self.task_service = TaskService()


    def get_tasks(self):
        try:
            tasks = self.task_service.get_tasks()
            return jsonify([asdict(task) for task in tasks]), 200
        except HTTPException as e:
            raise e


    def get_task(self, task_id):
        try:
            task = self.task_service.get_task(task_id)
            return jsonify(asdict(task)), 200
        except HTTPException as e:
            raise e


    def update_task(self, task_id):
        try:
            data = request.get_json()
            data["id"] = task_id
            task = self.task_service.update_task(Task(**data))
            return jsonify(asdict(task)), 200
        except HTTPException as e:
            raise e


    def create_task(self):
        try:
            data = request.get_json()
            task_obj = Task(**data)
            task = self.task_service.create_task(task_obj)
            return jsonify(asdict(task)), 201
        except HTTPException as e:
            raise e


    def delete_task(self, task_id):
        try:
            self.task_service.delete_task(task_id)
            return '', 204
        except HTTPException as e:
            raise e




