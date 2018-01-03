#!/usr/bin/python
from flask import Flask, flash, redirect \
    ,render_template, request, session, abort, url_for, g

from PythonApp import app, db
from models import User
from forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('main_page'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if  session.get('logged_in'):
        temp = User.query.filter_by(id=session.get('logged_in')).first()
        return redirect(url_for('main_page')

    if form.validate_on_submit():
        user = form.username.data
        password = form.password.datar
        temp = User.query.filter_by(username=user,password_hash=password).first()
        if  temp:
            session['logged_in'] = temp.id
            return redirect(url_for('main_page'))
        else:
            flash("Either the wrong user name or password")
            return render_template('login.html')
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('You were logged out')
    return redirect(url_for('index'))

@app.route("/main",methods=['GET', 'POST'])
def main_page():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    temp =  User.query.filter_by(id=session.get('logged_in')).first().reminder.all()
    return render_template('main.html',reminders=temp)

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('test.html', form=form)


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
