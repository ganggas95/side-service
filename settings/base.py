from datetime import timedelta
import os


class Base:
    SECRET_KEY = "b1sm1llah1290323***&&&@^#*@**24"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = os.getenv("PORT", 9091)
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    API_VERSION = os.getenv("API_VERSION", "v0.1")
    API_ROOT = f"/api/{API_VERSION}"
    JWT_TOKEN_LOCATION = "headers"
    JWT_CSRF_IN_COOKIES = False
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ACCESS_COOKIE_PATH = "{}{}".format(API_ROOT, "/auth/login")
    JWT_REFRESH_COOKIE_PATH = "{}{}".format(API_ROOT, '/auth/token/refresh')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)
    CORS_HEADERS = 'Content-Type, Authorization, Accept'
    ORIGINS = "*"
