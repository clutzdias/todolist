import sqlite3
import os
import logging

from ..models.task import Task



logging.basicConfig(level=logging.INFO)

DB_NAME = 'database.db'
DB_PATH = os.path.join(os.path.dirname(__file__), DB_NAME)


def init_db(app):
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        with app.open_resource('database/schema.sql') as f:
            conn.executescript(f.read().decode('utf8'))

        logging.info(f"Database {DB_NAME} created.")
        conn.commit()
        conn.close()


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


class TaskRepository:

    def create_task(self, task: Task):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tasks (title, description, completed) VALUES (:title, :description, :completed)',
            {
                'title': task.title,
                'description': task.description,
                'completed': task.completed
            }
        )
        
        conn.commit()
        task.id = cursor.lastrowid
        logging.info(f"Task created. Id: {task.id}")
        conn.close()
        return task


    def get_task(self, task_id: int) -> Task:
        conn = get_db_connection()
        task = conn.execute(
            'SELECT * FROM tasks WHERE id = :id',
            {'id': task_id}
        ).fetchone()
        conn.close()

        if task is None:
            logging.warning(f"Task with id {task_id} not found.")
            return None

        return Task(**task)
    
    def get_task_by_title(self, title: str) -> Task:
        conn = get_db_connection()
        task = conn.execute(
            'SELECT * FROM tasks WHERE title = :title',
            {'title': title}
        ).fetchone()
        conn.close()

        if task is None:
            logging.info(f"Task with title {title} not found.")
            return None

        return Task(**task)


    def get_tasks(self, only_completed: bool) -> list[Task]:
        conn = get_db_connection()

        sql = 'SELECT * FROM tasks'

        if only_completed:
            sql = 'SELECT * FROM tasks WHERE completed = true'
        
        tasks = conn.execute(sql).fetchall()
        conn.close()

        return [Task(**task) for task in tasks]


    def update_task(self, task: Task):
        conn = get_db_connection()
        conn.execute(
            'UPDATE tasks SET title = :title, description = :description, completed = :completed WHERE id = :id',
            {
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'id': task.id
            }
        )
        conn.commit()
        conn.close()

        logging.info(f"Task updated. Id: {task.id}")


    def delete_task(self, task_id: int):
        conn = get_db_connection()
        conn.execute('DELETE FROM tasks WHERE id = :id', {'id': task_id})
        conn.commit()
        conn.close()

        logging.info(f"Task deleted. Id: {task_id}")