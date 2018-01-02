import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DATABASE = 'sqlite:////tmp/pythonapptest.db' #tmp folder is deleted nightly
    DEBUG = True
    SECRET_KEY = "\xd2\xe2\xa8\xdf\xb2\x11\xe7\xd6\x86\xaf\x88"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'pythonapp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
