from settings.base import Base


class Local(Base):
    ENV = "development"
    DEBUG = True
