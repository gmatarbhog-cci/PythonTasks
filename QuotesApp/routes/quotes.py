from flask import Blueprint
from ..controllers.quotes import create_quote, get_quotes, update_quote, delete_quote, get_quote, get_quote_tags, like_quote, dislike_quote, remove_like_quote, remove_dislike_quote, get_quote_like_users

quotes = Blueprint('quote_blueprint', __name__)
# Quote routes
quotes.route('/', methods=['POST'])(create_quote)
quotes.route('/', methods=['GET'])(get_quotes)
quotes.route('/<id>', methods=['PATCH'])(update_quote)
quotes.route('/<id>', methods=['DELETE'])(delete_quote)
quotes.route('/<id>', methods=['GET'])(get_quote)
quotes.route('/tags', methods=['GET'])(get_quote_tags)

# User quote reaction routes
quotes.route('/<id>/like/up', methods=['PATCH'])(like_quote)
quotes.route('/<id>/dislike/up', methods=['PATCH'])(dislike_quote)
quotes.route('/<id>/like/down', methods=['PATCH'])(remove_like_quote)
quotes.route('/<id>/dislike/down', methods=['PATCH'])(remove_dislike_quote)

# User quote reaction data routes
quotes.route('/<quote_id>/like/users', methods=['GET'])(get_quote_like_users)
