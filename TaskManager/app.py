from flask import Flask
from .routes.task import task
from .db import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    print('Starting app')
    db.init_app(app)
    return app


app = create_app()
# Register route blueprints
app.register_blueprint(task, url_prefix='/task')
