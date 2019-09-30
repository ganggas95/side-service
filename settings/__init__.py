from settings import local
from settings import production
from settings import testing


app_config = {
    "local": local.Local,
    "production": production.Production,
    "testing": testing.Testing
}
