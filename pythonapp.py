from flask import Flask, flash, redirect, render_template, request, session, abort

 app = Flask(__name__)

 @app.route("/")
 def index():
     return render_template('index.html',name="Malik")
