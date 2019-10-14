from . import (desa_provider,
               kec_provider,
               kab_provider,
               prov_provider,
               user_provider,
               login_provider)


providers = [
    desa_provider.DesaProvider,
    kec_provider.KecProvider,
    kab_provider.KabProvider,
    prov_provider.ProvinsiProvider,
    login_provider.LoginProvider,
    user_provider.UserProvider,
]
