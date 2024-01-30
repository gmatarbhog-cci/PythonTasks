import uuid
import jwt
from flask import request, jsonify, make_response
from sqlalchemy.exc import SQLAlchemyError
from ..models.users import User
from ..database import db


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
        password=body['password'],
    )
    user.id = str(uuid.uuid4())
    try:
        db.session.add(user)
        db.session.commit()
        return make_response({'id': user.id}, 201)
    except SQLAlchemyError as e:
        print(e)
        return make_response({'error': "Error while creating the user."}, 500)
