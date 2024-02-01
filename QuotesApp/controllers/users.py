from flask import request, make_response
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash
from ..database import db
from ..models.users import users_schema, User
from ..common.authdecorator import token_required
from ..models.quotes import Quote, quotes_schema
from ..models.user_quote_reaction import UserQuoteReaction

@token_required
def get_users(self):
    return users_schema.dump(User.query.with_entities(User.id, User.first_name, User.last_name, User.email, User.deleted).all())


@token_required
def update_user(self, id):
    body = request.json
    try:
        query = db.session.query(User).filter(User.id == id)
        query.update(
            {'first_name': body['firstName'], 'last_name': body['lastName'], 'email': body['email'], 'password': generate_password_hash(body['password'])},
        )
        db.session.commit()
        return make_response({'id': id}, 200)
    except SQLAlchemyError as e:
        print(e)
        return make_response({'error': "Error while updating the user."}, 500)


@token_required
def delete_user(self, id):
    try:
        query = db.session.query(User).filter(User.id == id)
        query.update(
            {'deleted': 1},
        )
        db.session.commit()
        return make_response({'id': id}, 200)
    except SQLAlchemyError as e:
        print(e)
        return make_response({'error': "Error while deleting the user."}, 500)


@token_required
def get_user_quotes(self, id):
    return quotes_schema.dump(Quote.query.with_entities(Quote.id, Quote.quote).filter(Quote.user_id == id).all())


@token_required
def get_user_disliked_quotes(self, id):
    res = db.session.query(Quote).join(UserQuoteReaction).filter(UserQuoteReaction.user_id == id, UserQuoteReaction.dislike == True)
    return quotes_schema.dump(res)


@token_required
def get_user_liked_quotes(self, id):
    res = db.session.query(Quote).join(UserQuoteReaction).filter(UserQuoteReaction.user_id == id, UserQuoteReaction.like == True)
    return quotes_schema.dump(res)
