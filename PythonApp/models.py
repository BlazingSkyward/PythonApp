from datetime import datetime, timedelta
from PythonApp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    reminder = db.relationship('Reminder', backref='user', lazy='dynamic')
    #how the class is represented
    def __repr__(self):
        return '<User {}>'.format(self.username)

    def __init__(self,username,password_hash):
        self.username = username
        self.password_hash = password_hash

class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text,nullable=False)
    created_timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    completed_timestamp = db.Column(db.DateTime)
    due_timestamp = db.Column(db.DateTime,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    completed = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return '<Reminder {}>'.format(self.message)

    def __init__(self,message,date_time=datetime(2018,12,9)):
        self.message = message
        self.due_timestamp = date_time
