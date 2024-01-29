import json

from flask import request, abort, Response, jsonify
from ..models.task import Task, tasks_schema
from ..common.constants import status_const
from ..db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update


def get_tasks():
    result = tasks_schema.dump(Task.query.all())
    for task in result:
        task['status'] = status_const[task['status']]
    return result


def create_task():
    body = request.json
    task = Task(**body)
    try:
        db.session.add(task)
        db.session.commit()
        return jsonify({'id': task.id}), 201
    except SQLAlchemyError:
        return jsonify(error="Error while creating the task."), 500

