import os
import connexion
from connexion.resolver import RestyResolver
from extensions import ma
from extensions import jwt
from settings import app_config


def init_extension(app):
    jwt.init_app(app)
    ma.init_app(app)


def create_app(package):
    app = connexion.FlaskApp(
        package, 
        specification_dir='swagger/'
    )
    app.app.config.from_object(app_config[os.getenv('ENV', 'local')])
    init_extension(app.app)
    app.add_api(
        'users_app.yaml', 
        resolver=RestyResolver('api'), 
        arguments={
            "api_version": app.app.config["API_VERSION"],
            "base_url": app.app.config["API_ROOT"]
        }
    )
    return app
