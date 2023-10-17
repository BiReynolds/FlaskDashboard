from flask import render_template, flash, redirect, url_for, request
from ToQueue import app,db
from ToQueue.forms import TodoForm
from ToQueue.models import Task

@app.route('/')
@app.route('/index')
def index():
    todos=Task.query.order_by(Task.duedate.desc()).limit(5).all()
    return render_template('index.html',todos=todos)

@app.route('/addTask', methods = ['GET','POST'])
def addTask():
    form = TodoForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data,
                        priority=form.priority.data,
                        effort=form.effort.data,
                        duedate=form.duedate.data)
        db.session.add(new_task)
        db.session.commit()
        flash('New Task Added: {}'.format(form.title.data))
        return redirect(url_for('index'))
    return render_template('addTask.html', form = form)

@app.route('/task/<task_id>', methods = ['GET','POST'])
def task(task_id):
    task = Task.query.filter_by(id=task_id).first_or_404()
    if request.method == 'POST':
        task= Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
        flash('Task Deleted from Database: {}'.format(task.title))
        return redirect(url_for('index'))
    return render_template('task.html',task=task)