import os
import connexion
from connexion.resolver import RestyResolver
from injector import Binder
from flask_injector import FlaskInjector
from side_service.extensions import ma, jwt, db, migrate, cors, bcrypt
from side_service.settings import app_config
from side_service.provider import providers
from side_service.models.user import Users
from side_service.serializers.user_serializers import UserSerializers

__api_docs__ = [
    {"doc": "auth_app.yaml", "prefix": "auth"},
    {"doc": "users_app.yaml", "prefix": "users"},
    {"doc": "wilayah_app.yaml", "prefix": "wilayah"}
]


def init_extension(app):
    jwt.init_app(app)
    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    bcrypt.init_app(app)
    # schema.init_app(app)


def configure(binder: Binder):
    for provider in providers:
        binder.bind(provider, to=provider)


def create_app():
    app = connexion.App(
        __name__,
        specification_dir='swagger/'
    )
    app.app.config.from_object(app_config[os.getenv('ENV', 'local')])
    init_extension(app.app)
    for doc in __api_docs__:
        app.add_api(
            doc["doc"],
            resolver=RestyResolver('api'),
            arguments={
                "api_version": app.app.config["API_VERSION"],
                "base_url": f'{app.app.config["API_ROOT"]}/{doc["prefix"]}',
                "host": app.app.config["HOST"],
                "port": app.app.config["PORT"],
                "protocol": app.app.config["PROTOCOL"]
            }
        )
    FlaskInjector(app=app.app, modules=[configure])
    # app.add_error_handler(JsonValidationError, validation_error)
    return app.app


app = create_app()


@jwt.user_loader_callback_loader
def get_user(username):
    return Users.get_by_username(username)


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    user = Users.by_username(identity)
    return UserSerializers().dump(user)
