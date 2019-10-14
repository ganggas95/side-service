from side_service.models.kec import Kecamatan
from side_service.serializers.kec_serializers import KecSerializers
from .base_provider import Provider


class KecProvider(Provider):
    kec_seriazers = KecSerializers(many=True)

    @staticmethod
    def by_kode_kab(kode_prov):
        return Kecamatan.by_kode_kab(kode_prov)
