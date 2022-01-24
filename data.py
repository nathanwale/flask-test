from asyncio import Task
import db
import models

def all_tasks():
    rows = db.query("select * from Tasks order by created desc")
    return tasks_from_db_rows(rows)

def complete_tasks():
    rows = db.query("select * from CompleteTasks")
    return tasks_from_db_rows(rows)

def incomplete_tasks():
    rows = db.query("select * from IncompleteTasks")
    return tasks_from_db_rows(rows)

def task_by_id(id):
    rows = db.query("select * from Tasks where id = :id", {'id': id})
    return task_from_db_row(rows[0])


def tasks_from_db_rows(rows):
    return [task_from_db_row(row) for row in rows]


def task_from_db_row(row):
    (done, description, created, completed_on, id) = row
    return models.Task(
        id = id,
        description = description,
        done = done,
        completed_on = completed_on,
        created = created
    )

def create_task(description):
    db.procedure("new_task", [description])

def mark_task_complete(id):
    db.procedure("complete_task", {'id': id})

def mark_task_incomplete(id):
    db.procedure("undo_task", {'id': id})

def update_task_description(id, description):
    params = {
        'id': id,
        'description': description
    }
    db.procedure("redescribe_task", params)