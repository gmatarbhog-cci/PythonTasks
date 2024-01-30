from flask import Blueprint
from ..controllers.auth import sign_up

auth = Blueprint('auth_blueprint', __name__)

auth.route('/sign-up', methods=['POST'])(sign_up)
