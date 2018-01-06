#!/usr/bin/python
from flask import Flask, flash, redirect \
    ,render_template, request, session, abort, url_for, g

from PythonApp import app, db
from models import User,Reminder
from forms import LoginForm, NewForm, RegisterForm
from datetime import datetime

@app.route("/index")
@app.route("/")
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('main_page'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(prefix="Login")
    register = RegisterForm(prefix="Register")
    if  session.get('logged_in'):
        temp = User.query.filter_by(id=session.get('logged_in')).first()
        return redirect(url_for('main_page'))


    if form.validate_on_submit():
        user = form.username_log.data
        password = form.password_log.data
        temp = User.query.filter_by(username=user,password_hash=password).first()
        if  temp:
            session['logged_in'] = temp.id
            return redirect(url_for('main_page'))
        else:
            flash("Either the wrong user name or password")
            return redirect(url_for('login'))

    if register.validate_on_submit():
        user = register.username.data
        password = register.password.data
        email = register.email.data
        newUser = User(user,password,email)
        print newUser.id.__class__
        #db.session.add(newUser)
        #db.session.commit()

        #return redirect(url_for('login'))



    return render_template('login.html',form=form,register=register)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('index'))

@app.route("/main",methods=['GET', 'POST'])
def main_page():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    newForm = NewForm()
    user = User.query.filter_by(id=session.get('logged_in')).first()

    if request.method == 'POST':
        if newForm.validate():
            newReminder = Reminder(newForm.message.data,newForm.date.data)
            user.reminder.append(newReminder)
            db.session.commit()
            return redirect(url_for('main_page'))
        elif request.form.get('id'):
            editedReminder = user.reminder.filter_by(id=request.form.get('id')).first()
            editedReminder.completed_timestamp = datetime.now()
            print editedReminder
            db.session.commit()
            return redirect(url_for('main_page'))



    return render_template('main.html',reminders=user.reminder.all(), newForm=newForm)


#cannot find the correct method
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


#Cannot find the correct method
@app.errorhandler(405)
def page_not_found(e):
    return render_template("404.html")

#automatically logout when the app closes
#@app.teardown_appcontext
#def auto_logout(exception):
#    session.pop('logged_in',None)
