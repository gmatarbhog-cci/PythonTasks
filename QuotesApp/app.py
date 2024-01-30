from flask import Flask

from .routes.auth import auth
from .routes.quotes import quotes
from .routes.users import users
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    print('Starting app')
    db.init_app(app)
    return app


app = create_app()
# create database tables below
with app.app_context():
    db.create_all()
# Register route blueprints
app.register_blueprint(quotes, url_prefix='/quotes')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(users, url_prefix='/users')
