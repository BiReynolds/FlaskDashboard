from ToQueue import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    priority = db.Column(db.Integer, index = True)
    effort = db.Column(db.Integer, index = True)
    duedate = db.Column(db.Date)

    def __repr__(self):
        return '<Task {}>'.format(self.title)
    