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
        with app.open_resource('schema.sql') as f:
            conn.executescript(f.read().decode('utf8'))

        logging.info(f"Database {DB_NAME} created.")
        conn.commit()
        conn.close()


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_task(task: Task):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO tasks (name, description, completed) VALUES (:name, :description, :completed)',
        {
            'name': task.name,
            'description': task.description,
            'completed': task.completed
        }
    )
    conn.commit()
    task.id = cursor.lastrowid
    conn.close()
    return task