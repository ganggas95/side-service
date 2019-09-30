from flask_script import Manager
from factory import create_app

app = create_app(__name__).app
manager = Manager(app=app)


@manager.command
def runserver():
    app.run(
        app.config["HOST"],
        app.config["PORT"],
        debug=app.config["DEBUG"]
    )


if __name__ == '__main__':
    manager.run()
