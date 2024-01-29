from flask import Blueprint
from ..controllers.quotes import create_quote

quotes = Blueprint('quote_blueprint', __name__)

quotes.route('/', methods=['POST'])(create_quote)
