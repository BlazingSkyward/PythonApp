from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('password', validators=[InputRequired()], render_kw={"placeholder": "Password"})

class NewForm(FlaskForm):
    message = StringField('message', validators=[InputRequired()], render_kw={"placeholder":"This is what I have to remember"})
    date = DateTimeField('date',format="%m/%d/%Y %I:%M %p",validators=[InputRequired()], render_kw={"placeholder": "When it needs to be done(MM/DD/YYYY)"})
