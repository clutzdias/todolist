from flask import Flask
from flask_cors import CORS

from .database.task_repository import init_db

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:4200"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], supports_credentials=True)
    #app.config.from_object('config')
    
    from .routes import tasks_bp
    app.register_blueprint(tasks_bp)

    init_db(app)
    
    return app