from flask_bcrypt import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from sqlalchemy.ext.hybrid import hybrid_method
from sqlalchemy.ext.hybrid import hybrid_property

from . import db, BaseModel
from side_service.utils.passwd import hashed_password


class Users(db.Model, BaseModel):
    __tablename__ = "tb_users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    hashed_password = db.Column(db.Binary(60))
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, username, email, password=None):
        super(Users, self).__init__()
        self.username = username
        self.email = email
        if password:
            self.password = password

    def from_payload(self, payload):
        for key in payload:
            if not isinstance(payload[key], dict) or key != ["id", "password", "conf_password"]:
                setattr(self, key, payload[key])
            if key == 'password':
                self.create_password(payload[key])
    
    @property
    def is_exist(self):
        return self.by_username(self.username) is not None
    
    @staticmethod
    def all():
        return Users.query.all()

    @staticmethod
    def by_username(username: str) -> object:
        return Users.query.filter(
            Users.username == username
        ).first()

    @hybrid_property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password: str):
        self.hashed_password = generate_password_hash(password)
    
    @hybrid_method
    def check_password(self, password: str) -> bool:
        return check_password_hash(self.hashed_password, password)

    @property
    def access_token(self):
        return create_access_token(identity=self.username)

    @property
    def refresh_token(self):
        return create_refresh_token(identity=self.username)
