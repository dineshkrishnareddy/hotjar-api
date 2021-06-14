import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:fake_password@db:5432/logger'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
