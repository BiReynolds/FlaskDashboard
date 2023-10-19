from datetime import date,timedelta

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    priority = IntegerField('Priority (1-5)',default = 1)
    effort = IntegerField('Effort (1-5)', default = 1)
    duedate = DateField('Due Date (if applicable)', default = date.today()+timedelta(weeks = 52))
    submit = SubmitField('Add Task')

