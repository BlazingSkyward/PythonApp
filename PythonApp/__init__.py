from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.config.from_envvar('PYTHONAPP_SETTINGS', silent=True) #Since silent is true then nothing will occur if mess up
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from PythonApp import routes, models
