import json

from flask import request, abort, Response, jsonify
from ..models.task import Task, tasks_schema, task_schema
from ..common.constants import status_const
from ..db import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select


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


def update_task(id):
    body = request.json
    try:
        query = db.session.query(Task).filter(Task.id == id)
        query.update(body)
        db.session.commit()
        return jsonify({'id': id})
    except SQLAlchemyError:
        return jsonify(error="Error while updating the task."), 500


def delete_task(id):
    try:
        Task.query.filter(Task.id == id).delete()
        db.session.commit()
        return jsonify({'id': id})
    except SQLAlchemyError:
        return jsonify(error="Error while deleting the task."), 500


def get_task(id):
    result = Task.query.filter(Task.id == id).first()
    task = task_schema.dump(result)
    if not task:
        return jsonify(error="Not found."), 404
    task['status'] = status_const[task['status']]
    return task
