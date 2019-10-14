from flask_marshmallow import Schema


class KecSerializers(Schema):

    class Meta:
        fields = [
            'kode_kec',
            'name',
        ]
