from flask import request, jsonify
from ..common.authdecorator import token_required
from ..models.quotes import Quote, quote_schema, quotes_schema, users_quote_liked
from ..models.users import User
from ..models.user_quote_reaction import UserQuoteReaction
from ..database import db
from sqlalchemy.exc import SQLAlchemyError
import uuid


@token_required
def create_quote(data):
    body = request.json
    quote = Quote(**body)
    quote.id = str(uuid.uuid4())
    quote.user_id = request.headers.user_id
    try:
        db.session.add(quote)
        db.session.commit()
        return jsonify({'id': quote.id}), 201
    except SQLAlchemyError as e:
        print(e)
        return jsonify(error="Error while creating the quote."), 500


def get_quotes():
    return quotes_schema.dump(Quote.query.all())


@token_required
def update_quote(self, id):
    body = request.json
    try:
        query = db.session.query(Quote).filter(Quote.id == id)
        query.update(body)
        db.session.commit()
        return jsonify({'id': id})
    except SQLAlchemyError:
        return jsonify(error="Error while updating the quote."), 500


@token_required
def delete_quote(self, id):
    try:
        Quote.query.filter(Quote.id == id).delete()
        db.session.commit()
        return jsonify({'id': id})
    except SQLAlchemyError:
        return jsonify(error="Error while deleting the quote."), 500


@token_required
def get_quote(self, id):
    result = Quote.query.filter(Quote.id == id).first()
    quote = quote_schema.dump(result)
    if not quote:
        return jsonify(error="Not found."), 404
    return quote


@token_required
def get_quote_tags(self):
    return quotes_schema.dump(Quote.query.with_entities(Quote.id, Quote.tags).all())


@token_required
def like_quote(self, id):
    try:
        quote = Quote.query.filter(Quote.id == id).first()
        if not quote:
            return jsonify(error="Quote not found."), 404

        quote_reaction = UserQuoteReaction(id=str(uuid.uuid4()), like=True, quote_id=id, user_id=request.headers.user_id)

        query = db.session.query(UserQuoteReaction).filter(UserQuoteReaction.quote_id == id, UserQuoteReaction.user_id == request.headers.user_id)
        if query.first() is None:
            db.session.add(quote_reaction)
        else:
            query.update({'like': True})
        db.session.commit()
        return jsonify({'id': id})
    except SQLAlchemyError:
        return jsonify(error="Error while liking the quote."), 500


@token_required
def dislike_quote(self, id):
    try:
        quote = Quote.query.filter(Quote.id == id).first()
        if not quote:
            return jsonify(error="Quote not found."), 404

        quote_reaction = UserQuoteReaction(id=str(uuid.uuid4()), dislike=True, quote_id=id, user_id=request.headers.user_id)

        query = db.session.query(UserQuoteReaction).filter(UserQuoteReaction.quote_id == id, UserQuoteReaction.user_id == request.headers.user_id)
        if query.first() is None:
            db.session.add(quote_reaction)
        else:
            query.update({'dislike': True})
        db.session.commit()
        return jsonify({'id': id})
    except SQLAlchemyError:
        return jsonify(error="Error while disliking the quote."), 500


@token_required
def remove_like_quote(self, id):
    try:
        quote = Quote.query.filter(Quote.id == id).first()
        if not quote:
            return jsonify(error="Quote not found."), 404

        quote_reaction = UserQuoteReaction(id=str(uuid.uuid4()), like=False, quote_id=id, user_id=request.headers.user_id)

        query = db.session.query(UserQuoteReaction).filter(UserQuoteReaction.quote_id == id, UserQuoteReaction.user_id == request.headers.user_id)
        if query.first() is None:
            db.session.add(quote_reaction)
        else:
            query.update({'like': False})
        db.session.commit()
        return jsonify({'id': id})
    except SQLAlchemyError:
        return jsonify(error="Error while removing the like for the quote."), 500


@token_required
def remove_dislike_quote(self, id):
    try:
        quote = Quote.query.filter(Quote.id == id).first()
        if not quote:
            return jsonify(error="Quote not found."), 404

        quote_reaction = UserQuoteReaction(id=str(uuid.uuid4()), dislike=False, quote_id=id, user_id=request.headers.user_id)

        query = db.session.query(UserQuoteReaction).filter(UserQuoteReaction.quote_id == id, UserQuoteReaction.user_id == request.headers.user_id)
        if query.first() is None:
            db.session.add(quote_reaction)
        else:
            query.update({'dislike': False})
        db.session.commit()
        return jsonify({'id': id})
    except SQLAlchemyError:
        return jsonify(error="Error while removing the dislike for the quote."), 500


@token_required
def get_quote_like_users(self, quote_id):
    res = db.session.query(User).join(UserQuoteReaction).filter(UserQuoteReaction.quote_id == quote_id, UserQuoteReaction.like==True)
    return users_quote_liked.dump(res)
