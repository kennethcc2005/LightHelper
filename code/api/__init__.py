from .users.users import users
from flask import app

app.register_blueprint(users)