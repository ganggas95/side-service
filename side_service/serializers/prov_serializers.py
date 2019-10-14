from flask_marshmallow import Schema


class ProvSerializers(Schema):

    class Meta:
        fields = [
            'kode_prov',
            'name',
        ]
