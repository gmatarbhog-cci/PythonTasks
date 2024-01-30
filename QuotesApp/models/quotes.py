from ..database import db
from marshmallow import fields, Schema


class Quote(db.Model):
    __tablename__ = 'quotes'

    id = db.Column(db.String(100), primary_key=True)
    quote = db.Column(db.String(255))
    author = db.Column(db.String(50))
    tags = db.Column(db.String(255))
    user_id = db.Column(db.String(100))


class QuoteSchema(Schema):
    id = fields.String()
    quote = fields.String()
    author = fields.String()
    tags = fields.String()
    user_id = fields.String()


quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)
