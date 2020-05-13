from FlaskApp import app
from flask_script import Manager
from FlaskApp.scripts.db import InitDB

if __name__ == '__main__':
    app.run(host='192.168.33.11', port=5000)
    manager = Manager()
    manager.add_command('init_db', InitDB)
    manager.run()
