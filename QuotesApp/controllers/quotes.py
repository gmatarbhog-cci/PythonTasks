from flask import request, jsonify
from ..models.quotes import Quote, quote_schema, quotes_schema
from ..database import db
from sqlalchemy.exc import SQLAlchemyError
import uuid


def create_quote():
    body = request.json
    quote = Quote(**body)
    quote.id = str(uuid.uuid4())
    try:
        db.session.add(quote)
        db.session.commit()
        return jsonify({'id': quote.id}), 201
    except SQLAlchemyError as e:
        print(e)
        return jsonify(error="Error while creating the quote."), 500


def get_quotes():
    return quotes_schema.dump(Quote.query.all())


def update_quote(id):
    body = request.json
    try:
        query = db.session.query(Quote).filter(Quote.id == id)
        query.update(body)
        db.session.commit()
        return jsonify({'id': id})
    except SQLAlchemyError:
        return jsonify(error="Error while updating the quote."), 500
