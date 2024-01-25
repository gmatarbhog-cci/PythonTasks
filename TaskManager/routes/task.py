from flask import Blueprint

from ..controllers.task import get_tasks

task = Blueprint('task_blueprint', __name__)

task.route('/', methods=['GET'])(get_tasks)
