from flask import request
from flask_injector import inject
from side_service.provider import desa_provider
from side_service.provider import kec_provider
from side_service.provider import kab_provider
from side_service.provider import prov_provider


@inject
def list_desa(desa_provider: desa_provider.DesaProvider, kode_kec) -> dict:

    serializers = desa_provider.desa_seriazers.dump(
        desa_provider.by_kode_kec(kode_kec))

    return desa_provider.create_response(
        status=200,
        data=serializers,
        msg="Success get data desa"
    )


@inject
def list_kec(kec_provider: kec_provider.KecProvider, kode_kab) -> dict:

    serializers = kec_provider.kec_seriazers.dump(
        kec_provider.by_kode_kab(kode_kab))

    return kec_provider.create_response(
        status=200,
        data=serializers,
        msg="Success get data kec"
    )


@inject
def list_kab(kab_provider: kab_provider.KabProvider, kode_prov) -> dict:

    serializers = kab_provider.kab_seriazers.dump(
        kab_provider.by_kode_prov(kode_prov))

    return kab_provider.create_response(
        status=200,
        data=serializers,
        msg="Success get data kab"
    )


@inject
def list_prov(prov_provider: prov_provider.ProvinsiProvider) -> dict:

    serializers = prov_provider.prov_seriazers.dump(prov_provider.all())

    return prov_provider.create_response(
        status=200,
        data=serializers,
        msg="Success get data kab"
    )
