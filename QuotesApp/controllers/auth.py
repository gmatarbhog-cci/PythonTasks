import uuid
from datetime import datetime, timedelta, timezone

import jwt
from flask import request, jsonify, make_response
from sqlalchemy.exc import SQLAlchemyError

from ..config import SECRET_KEY
from ..models.users import User
from ..database import db
from  werkzeug.security import generate_password_hash, check_password_hash

def sign_up():
    body = request.json
    email, password = body['email'], body['password']
    user_exists = User.query.filter(User.email == email).first()
    if user_exists:
        return make_response({'error': 'User exists'}, 400)
    user = User(
        first_name=body['firstName'],
        last_name=body['lastName'],
        email=body['email'],
        password=generate_password_hash(body['password']),
    )
    user.id = str(uuid.uuid4())
    try:
        db.session.add(user)
        db.session.commit()
        return make_response({'id': user.id}, 201)
    except SQLAlchemyError as e:
        print(e)
        return make_response({'error': "Error while creating the user."}, 500)


def sign_in():
    body = request.json
    email, password = body['email'], body['password']
    user = User.query.filter(User.email == email).first()
    if not user:
        return make_response({'error': 'User with the given email does not exist.'}, 400)
    if check_password_hash(user.password, body['password']):
        # generate token
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.now(timezone.utc) + timedelta(minutes=30)
        }, SECRET_KEY)
        return make_response({'token': token}, 200)
    return make_response({'error': 'Credentials do not match!!'})
