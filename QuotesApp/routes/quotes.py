from flask import Blueprint
from ..controllers.quotes import create_quote, get_quotes, update_quote, delete_quote, get_quote

quotes = Blueprint('quote_blueprint', __name__)

quotes.route('/', methods=['POST'])(create_quote)
quotes.route('/', methods=['GET'])(get_quotes)
quotes.route('/<id>', methods=['PATCH'])(update_quote)
quotes.route('/<id>', methods=['DELETE'])(delete_quote)
quotes.route('/<id>', methods=['GET'])(get_quote)
