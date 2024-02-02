from flask import Flask

from .controllers.quotes import update_like_dislike_count
from .routes.auth import auth
from .routes.authors import authors
from .routes.quotes import quotes
from .routes.users import users
from .database import db
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()
scheduler.add_job(update_like_dislike_count, 'interval', minutes=1, id='my_job_id')


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
app.register_blueprint(authors, url_prefix='/authors')
