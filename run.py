from flask_script import Manager
from courseoffering.app import app

manager = Manager(app)


@manager.command
def run():
    app.run(debug=True)


if __name__ == "__main__":
    manager.run()
