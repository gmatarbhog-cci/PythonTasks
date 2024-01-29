from flask import Blueprint
from ..controllers.task import get_tasks, create_task, update_task, delete_task, get_task

task = Blueprint('task_blueprint', __name__)

task.route('/', methods=['GET'])(get_tasks)
task.route('/', methods=['POST'])(create_task)
task.route('/<id>', methods=['PATCH'])(update_task)
task.route('/<id>', methods=['DELETE'])(delete_task)
task.route('/<id>', methods=['GET'])(get_task)
