from sqlalchemy import text

from ..database import db
from marshmallow import fields, Schema


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(100), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(55))
    password = db.Column(db.String(255))
    deleted = db.Column(db.Boolean, server_default=text('0'))

class UserSchema(Schema):
    id = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.String()
    password = fields.String()
    deleted = fields.Boolean()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
