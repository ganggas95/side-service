from side_service.models.kab import Kabupaten
from side_service.serializers.kab_serializers import KabSerializers
from .base_provider import Provider


class KabProvider(Provider):
    kab_seriazers = KabSerializers(many=True)

    @staticmethod
    def by_kode_prov(kode_prov):
        return Kabupaten.by_kode_prov(kode_prov)
