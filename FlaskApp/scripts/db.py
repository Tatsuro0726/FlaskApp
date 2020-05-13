from flask_script import Command
from FlaskApp import db

class InitDB(Command):

    def run(self):
        db.create_all()