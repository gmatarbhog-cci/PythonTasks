from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from ..database import db
from marshmallow import fields, Schema


class Quote(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.String(100), primary_key=True)
    quote = db.Column(db.String(255))
    author = db.Column(db.String(50))
    tags = db.Column(db.String(255))
    user_id = db.Column(db.String(100), ForeignKey('users.id'))
    users = relationship("User", secondary="user_quote_reaction", back_populates="quotes")


class QuoteSchema(Schema):
    id = fields.String()
    quote = fields.String()
    author = fields.String()
    tags = fields.String()
    user_id = fields.String()


class UsersQuoteLikedSchema(Schema):
    quote_id = fields.String()
    user_id = fields.String(attribute='id')
    first_name = fields.String()


quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)
users_quote_liked = UsersQuoteLikedSchema(many=True)
