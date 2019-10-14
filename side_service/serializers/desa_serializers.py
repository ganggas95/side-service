from flask_marshmallow import Schema


class DesaSerializers(Schema):

    class Meta:
        fields = [
            'kode_desa',
            'name',
        ]
