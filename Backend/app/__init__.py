from flask import Flask

from .database.task_repository import init_db

def create_app():
    app = Flask(__name__)
    #app.config.from_object('config')
    
    from .routes import tasks_bp
    app.register_blueprint(tasks_bp)

    init_db(app)
    
    return app