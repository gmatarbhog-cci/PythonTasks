from flask import Blueprint
from ..controllers.quotes import get_quote_authors

authors = Blueprint('author_blueprint', __name__)

authors.route('/', methods=['GET'])(get_quote_authors)
