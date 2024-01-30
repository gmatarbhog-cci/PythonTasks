from ..models.users import users_schema, User
from ..common.authdecorator import token_required


@token_required
def get_users(self):
    return users_schema.dump(User.query.with_entities(User.id, User.first_name, User.last_name, User.email).all())
