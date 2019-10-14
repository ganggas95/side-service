from flask_marshmallow import Schema


class KabSerializers(Schema):

    class Meta:
        fields = [
            'kode_kab',
            'name',
        ]
