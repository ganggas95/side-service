from settings.base import Base


class Production(Base):
    ENV = "production"
    DEBUG = False
