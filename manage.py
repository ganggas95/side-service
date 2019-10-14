from flask_script import Manager
from side_service import app
from side_service.models.user import Users
from side_service.utils import importer


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
        user.password = password
    user.save()


@manager.command
def default_provinces():
    import_provinces = importer.ImportProvinceFile("provinces.csv")
    import_provinces.read_data()


@manager.command
def default_regencies():
    import_regencies = importer.ImportRegenciesFile("regencies.csv")
    import_regencies.read_data()


@manager.command
def default_districts():
    import_districts = importer.ImportDistrictFile("districts.csv")
    import_districts.read_data()


@manager.command
def default_villages():
    import_villages = importer.ImportVillagesFile("villages.csv")
    import_villages.read_data()


@manager.command
def runserver():
    app.run(
        app.config["HOST"],
        app.config["PORT"],
        debug=app.config["DEBUG"]
    )


if __name__ == '__main__':
    manager.run()
