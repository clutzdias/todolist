from flask import Flask

def create_app():
    app = Flask(__name__)
    #app.config.from_object('config')
    
    from . import routes
    app.register_blueprint(routes.tasks_bp, url_prefix='/api')
    
    return app