from side_service.settings.base import Base


class Testing(Base):
    ENV = "testing"
    DEBUG = True
    PROTOCOL = "http"
