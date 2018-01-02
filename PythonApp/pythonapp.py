from PythonApp import app, db
from PythonApp.models import User, Reminder

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Reminder': Reminder}
