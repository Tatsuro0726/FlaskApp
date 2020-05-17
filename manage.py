from flask_script import Manager
from FlaskApp import app,db
from flask_migrate import Migrate, MigrateCommand

# from FlaskApp.scripts.db import InitDB


if __name__ == "__main__":
    migrate = Migrate(app,db)
    manager = Manager(app)
    # manager.add_command('init_db', InitDB)
    manager.add_command('db',MigrateCommand)
    manager.run()