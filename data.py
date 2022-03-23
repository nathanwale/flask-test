import db
from datetime import datetime
from models import Task
from sqlalchemy import select

def all_tasks():
    statement = select(Task)
    return db.run(statement)

def complete_tasks():
    statement = select(Task).filter_by(done = True).order_by(Task.completed_on.desc())
    return db.run(statement)

def incomplete_tasks():
    statement = select(Task).filter_by(done = False).order_by(Task.created.desc())
    return db.run(statement)

def task_by_id(id):
    return db.get(Task, id)


def create_task(description):
    task = Task(description=description)
    db.add(task)


def mark_task_complete(id):
    with db.update(Task, id) as task:
        task.done = True 
        task.completed_on = datetime.now()

def mark_task_incomplete(id):
    with db.update(Task, id) as task:
        task.done = False 
        task.completed_on = None

def update_task_description(id, description):
    with db.update(Task, id) as task:
        task.description = description