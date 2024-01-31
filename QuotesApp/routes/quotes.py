from flask import Blueprint
from ..controllers.quotes import create_quote, get_quotes, update_quote, delete_quote, get_quote, get_quote_tags, like_quote, dislike_quote, remove_like_quote, remove_dislike_quote

quotes = Blueprint('quote_blueprint', __name__)
# Quote routes
quotes.route('/', methods=['POST'])(create_quote)
quotes.route('/', methods=['GET'])(get_quotes)
quotes.route('/<id>', methods=['PATCH'])(update_quote)
quotes.route('/<id>', methods=['DELETE'])(delete_quote)
quotes.route('/<id>', methods=['GET'])(get_quote)
quotes.route('/tags', methods=['GET'])(get_quote_tags)

# User quote reaction Routes
quotes.route('/<id>/like/up', methods=['PATCH'])(like_quote)
quotes.route('/<id>/dislike/up', methods=['PATCH'])(dislike_quote)
quotes.route('/<id>/like/down', methods=['PATCH'])(remove_like_quote)
quotes.route('/<id>/dislike/down', methods=['PATCH'])(remove_dislike_quote)
