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
