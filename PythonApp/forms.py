from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateTimeField
from wtforms.validators import InputRequired, EqualTo, Email

class LoginForm(FlaskForm):
    username_log = StringField('username', validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password_log = PasswordField('password', validators=[InputRequired()], render_kw={"placeholder": "Password"})

class NewForm(FlaskForm):
    message = StringField('message', validators=[InputRequired()], render_kw={"placeholder":"This is what I have to remember"})
    date = DateTimeField('date',format="%m/%d/%Y %I:%M %p",validators=[InputRequired()], render_kw={"placeholder": "When it needs to be done(MM/DD/YYYY)"})

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('New Password', [
        InputRequired(),
        EqualTo('confirm', message='Passwords must match')
    ], render_kw={"placeholder": "Password"})
    confirm = PasswordField('Repeat Password',render_kw={"placeholder": "Repeat Password"})
    email = StringField('Email',validators=[Email()],render_kw={"placeholder": "Valid Email Address"})
