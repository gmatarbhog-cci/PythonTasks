from flask import Blueprint
from ..controllers.users import get_users, update_user

users = Blueprint('user_blueprint', __name__)

users.route('/', methods=['GET'])(get_users)
users.route('/<id>', methods=['PATCH'])(update_user)
