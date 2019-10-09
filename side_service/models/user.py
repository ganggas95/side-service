from bcrypt import hashpw, checkpw, gensalt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from side_service import db
from side_service.utils.passwd import hashed_password


class Users(db.Model):
    __tablename__ = "tb_users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(500))

    def __init__(self, username, email, password=None):
        super(Users, self).__init__()
        self.username = username
        self.email = email
        if password:
            self.create_password(password)

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

    def create_password(self, password: str):
        self.password = hashpw(
            hashed_password(password), gensalt()
        )
    
    def check_password(self, password: str) -> bool:
        return checkpw(
            hashed_password(password),
            str(self.password).encode('utf-8')
        )

    @property
    def access_token(self):
        return create_access_token(identity=self.username)

    @property
    def refresh_token(self):
        return create_refresh_token(identity=self.username)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.add(self)
        db.session.commit()
