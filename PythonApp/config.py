import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DATABASE = '/tmp/pythonapp.db' #tmp folder is deleted nightly
    DEBUG = False
    SECRET_KEY = "q\xd2\xe2\xa8\xdf3\xb2\x11\xe7K/:\xd6\x86\xaf\x88"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'pythonapp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
