from sqlalchemy import text, ForeignKey
from ..database import db
from marshmallow import fields, Schema


class UserQuoteReaction(db.Model):
    __tablename__ = 'user_quote_reaction'

    id = db.Column(db.String(100), primary_key=True)
    like = db.Column(db.Boolean(), server_default=text('0'))
    dislike = db.Column(db.Boolean(), server_default=text('0'))
    quote_id = db.Column(db.String(100), ForeignKey('quotes.id'))
    user_id = db.Column(db.String(100), ForeignKey('users.id'))


class UserQuoteReactionSchema(Schema):
    id = fields.String()
    like = fields.Boolean()
    dislike = fields.Boolean()
    quote_id = fields.String()
    user_id = fields.String()


user_quote_reaction_schema = UserQuoteReactionSchema()
user_quote_reactions_schema = UserQuoteReactionSchema(many=True)
