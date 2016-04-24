from flask import Flask, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import flask.ext.login as flask_login
from api.users.users import users

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config.get('LOGIN_SECRET_KEY')
app.register_blueprint(users)

db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


# home page
@app.route('/')
def index():

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
