from side_service.models.desa import Desa
from side_service.serializers.desa_serializers import DesaSerializers
from .base_provider import Provider

class DesaProvider(Provider):
    desa_seriazers = DesaSerializers(many=True)

    @staticmethod
    def by_kode_kec(kode_kec):
        return Desa.by_kode_kec(kode_kec)
