from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_user import UserManager
from FlaskApp.models.user import User
from flask_migrate import Migrate


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
user_manager = UserManager(app, db, User)
migrate = Migrate(app, db)

@app.cli.command('initdb')
def initdb_command():
    db.create_all()

from FlaskApp.views import views
