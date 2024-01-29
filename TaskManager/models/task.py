from ..db import db
from marshmallow import fields, Schema


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    status = db.Column(db.Integer)


class TaskSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    status = fields.Integer()


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
