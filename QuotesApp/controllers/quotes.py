import json

from flask import request, jsonify

from ..common.authdecorator import token_required
from ..models.quotes import Quote, quote_schema, quotes_schema
from ..database import db
from sqlalchemy.exc import SQLAlchemyError
import uuid

from ..models.users import User


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
