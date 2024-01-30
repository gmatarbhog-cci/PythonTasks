from flask import Blueprint
from ..controllers.auth import sign_up, sign_in

auth = Blueprint('auth_blueprint', __name__)

auth.route('/sign-up', methods=['POST'])(sign_up)
auth.route('/sign-in', methods=['POST'])(sign_in)
