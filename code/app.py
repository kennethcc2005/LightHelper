from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager
import flask.ext.login as flask_login
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config.get('LOGIN_SECRET_KEY')

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
