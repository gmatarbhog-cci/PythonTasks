from flask import Blueprint
from ..controllers.users import get_users, update_user, delete_user, get_user_quotes, get_user_disliked_quotes, get_user_liked_quotes

users = Blueprint('user_blueprint', __name__)

users.route('/', methods=['GET'])(get_users)
users.route('/<id>', methods=['PATCH'])(update_user)
users.route('/<id>', methods=['DELETE'])(delete_user)

# User quote routes
users.route('/<id>/quotes', methods=['GET'])(get_user_quotes)
users.route('/<id>/unfavourite-quotes', methods=['GET'])(get_user_disliked_quotes)
users.route('/<id>/favourite-quotes', methods=['GET'])(get_user_liked_quotes)
