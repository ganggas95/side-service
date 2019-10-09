from flask_script import Manager
from side_service import app
from side_service.models.user import Users


manager = Manager(app=app)


@manager.command
def create_default_user():
    username = "admin"
    email = "admin@li.com"
    password = "admin212"
    user = Users.by_username(username)
    if user is None:
        user = Users(username, email, password)
    else:
        user.create_password(password)
    user.save()


@manager.command
def runserver():
    app.run(
        app.config["HOST"],
        app.config["PORT"],
        debug=app.config["DEBUG"]
    )


if __name__ == '__main__':
    manager.run()
