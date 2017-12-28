#!/usr/bin/python
from flask import Flask, flash, redirect \
    ,render_template, request, session, abort, url_for, g

from PythonApp import app

#import os
#import time
#from datetime import datetime

#app = Flask(__name__)
#app.config.from_object(Config)


@app.route("/")
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('main_page'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('main'))

    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if user == 'admin' and password == 'password':
            session['logged_in'] = user
            return redirect(url_for('main_page'))
        else:
            return render_template('login.html')
    return render_template('login.html')

@app.route("/main") #,methods=['GET', 'POST'])
def main_page():
    return render_template('main.html')

#cannot find the correct method
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


#Cannot find the correct method
@app.errorhandler(405)
def page_not_found(e):
    return render_template("404.html")
