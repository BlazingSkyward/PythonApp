from datetime import datetime
from PythonApp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    #how the class is represented
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text,nullable=False)
    created_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    completed_timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    completed = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return '<Reminder {}>'.format(self.message)
