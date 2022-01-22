from flask import Flask, render_template, redirect, request
import data


app = Flask(__name__)

#
# Form for new tasks
#
@app.route('/task/new', methods=['GET'])
def task_form():
    return render_template('task-form.html')

#
# Create a task
#
@app.route('/task/create', methods=['POST'])
def create_task():
    description = request.form['description']
    data.create_task(description)
    return redirect('/')

#
# View a task
#
@app.route('/task/<id>/view/', methods=['GET'])
def view_task(id):
    task = data.task_by_id(id)
    return render_template('task.html', task=task)

#
# View all tasks
#    
@app.route('/')
@app.route('/tasks/', methods=['GET'])
def view_tasks():
    incomplete_tasks = data.incomplete_tasks()
    complete_tasks = data.complete_tasks()
    return render_template(
        'task-list.html', 
        incomplete_tasks=incomplete_tasks,
        complete_tasks=complete_tasks)

#
# Mark as done
#
@app.route('/task/<id>/complete/', methods=['POST'])
def mark_task_complete(id):
    data.mark_task_complete(id)
    return redirect('/')

#
# Mark as incomplete
#
@app.route('/task/<id>/undo/', methods=['POST'])
def mark_task_incomplete(id):
    data.mark_task_incomplete(id)
    return redirect('/')

#
# Date filter
#
@app.template_filter('date')
def datetime_format(value, format="%b %d %Y"):
    return value.strftime(format)



#
# Run
#
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=8080, debug=True)