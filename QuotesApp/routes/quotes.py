from flask import Blueprint
from ..controllers.quotes import create_quote, get_quotes

quotes = Blueprint('quote_blueprint', __name__)

quotes.route('/', methods=['POST'])(create_quote)
quotes.route('/', methods=['GET'])(get_quotes)
