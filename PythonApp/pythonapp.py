#!/usr/bin/python
from flask import Flask, flash, redirect \
    ,render_template, request, session, abort, url_for, g

import os
import time
from datetime import datetime


DEBUG = False
TESTING = False
SECRET_KEY = "q\xd2\xe2\xa8\xdf3\xb2\x11\xe7K/:\xd6\x86\xaf\x88"

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('main_page'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('/'))

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")
