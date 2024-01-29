from flask import Flask
from .routes.quotes import quotes
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    print('Starting app')
    db.init_app(app)
    return app


app = create_app()
with app.app_context():
    db.create_all()
# Register route blueprints
app.register_blueprint(quotes, url_prefix='/quotes')
