from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
# from flask_json_schema import JsonSchema

jwt = JWTManager()
ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
# schema = JsonSchema()
