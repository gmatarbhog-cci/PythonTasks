from functools import wraps
from flask import request, jsonify
import jwt
from ..models.users import User
from ..config import SECRET_KEY


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'authorization' in request.headers:
            token = request.headers['authorization']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing!!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user = User.query.filter(User.id == data['user_id']).first()
            request.headers.user_id = user.id
        except Exception as e:
            print(e)
            return jsonify({
                'message': 'Token is invalid!!'
            }), 401
        # return user
        return f(user, *args, **kwargs)

    return decorated
