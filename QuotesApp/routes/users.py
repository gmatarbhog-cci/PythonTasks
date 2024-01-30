from flask import Blueprint
from ..controllers.users import get_users

users = Blueprint('user_blueprint', __name__)

users.route('/', methods=['GET'])(get_users)
