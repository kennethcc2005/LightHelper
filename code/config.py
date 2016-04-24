import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/givelight_local'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
LOGIN_SECRET_KEY = 'givelight2016'