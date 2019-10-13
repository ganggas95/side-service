from side_service.settings.base import Base


class Production(Base):
    ENV = "production"
    DEBUG = False
    PROTOCOL = "https"
