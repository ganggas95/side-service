from side_service.models.prov import Provinsi
from side_service.serializers.prov_serializers import ProvSerializers
from .base_provider import Provider


class ProvinsiProvider(Provider):
    prov_seriazers = ProvSerializers(many=True)

    @staticmethod
    def all():
        return Provinsi.all()
