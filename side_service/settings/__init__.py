from side_service.settings import local
from side_service.settings import production
from side_service.settings import testing


app_config = {
    "local": local.Local,
    "production": production.Production,
    "testing": testing.Testing
}
